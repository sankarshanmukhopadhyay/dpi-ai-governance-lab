from pathlib import Path
import yaml

ROOT=Path('case-studies/digital-statecraft-benefit-closure')

def evaluate(s):
    i=s.get('inputs',{})
    cap=s.get('capability')
    if cap in ('integrated','CAP-AUTHORITY-BOUNDED-DELEGATION'):
        if i.get('delegation_status')=='revoked': return 'deny','delegation_revoked'
        if i.get('action') and i.get('action')!='determine-benefit-eligibility': return 'deny','action_out_of_scope'
    if cap=='CAP-INTERINSTITUTIONAL-ADMISSIBILITY' and i.get('evidence_authentic') and not i.get('evidence_admissible'): return 'deny','purpose_not_admissible'
    if cap=='CAP-INFERENCE-TRACEABILITY':
        if i.get('expected_model_version') and i.get('model_version')!=i.get('expected_model_version'): return 'deny','inference_version_mismatch'
        if i.get('expected_threshold') is not None and i.get('threshold')!=i.get('expected_threshold'): return 'deny','threshold_mismatch'
    if cap=='CAP-REDRESS-APPEAL' and i.get('redress_available') is False: return 'fail','redress_unavailable'
    if cap=='CAP-CORRECTION-PROPAGATION' and i.get('completed_targets',0)<i.get('mandatory_targets',0): return 'partial','mandatory_target_failed'
    if cap=='CAP-EVIDENCE-CLOSURE' and i.get('effect_correlation') is False: return 'fail','effect_correlation_missing'
    return 'allow',None

def main():
    profile=yaml.safe_load((ROOT/'system-profile.yaml').read_text())
    evidence=yaml.safe_load((ROOT/'implementation-evidence.yaml').read_text())
    scenarios=yaml.safe_load((ROOT/'adversarial-scenarios.yaml').read_text())['scenarios']
    closure=yaml.safe_load((ROOT/'closure-evidence.yaml').read_text())
    failures=[]
    required_caps=set(profile['selected_capabilities'])
    closure_caps={c['capability_id'] for c in closure['capabilities']}
    if required_caps!=closure_caps: failures.append('closure capability set does not match selected capabilities')
    if closure.get('status')!='closed': failures.append('fixture closure status must be closed')
    if any(c.get('result')!='pass' for c in closure['capabilities']): failures.append('all selected capabilities must pass fixture closure')
    if any(c.get('result')!='pass' for c in closure['acceptance_criteria']): failures.append('all acceptance criteria must pass')
    if evidence['runtime_authorization']['effect_ref']!='payment:BEN-001': failures.append('effect authorization correlation missing')
    if evidence['decision_receipt']['inference_trace_ref']!=evidence['inference_trace']['trace_id']: failures.append('decision/inference trace mismatch')
    if evidence['correction']['execution_receipt']['status']!='complete': failures.append('successful correction must be complete')
    for s in scenarios:
        got=evaluate(s); exp=(s['expected'],s.get('reason'))
        if got!=exp: failures.append(f"{s['id']}: expected {exp}, got {got}")
        print(f"{s['id']}: {got}")
    required_negative={'delegated-action-out-of-scope','delegation-revoked','authentic-but-inadmissible','model-version-mismatch','threshold-mismatch','unavailable-redress','correction-partial-failure','effect-authorization-broken'}
    if not required_negative.issubset({s['id'] for s in scenarios}): failures.append('required negative scenario coverage incomplete')
    if failures:
        [print('FAIL:',f) for f in failures]; return 2
    print(f"Digital Statecraft benefit closure fixture PASS: {len(required_caps)} capabilities, {len(scenarios)} scenarios")
    return 0
if __name__=='__main__': raise SystemExit(main())

---
layout: default
title: Operator playbook
nav_order: 2
---

# Operator playbook

Use this path when you are implementing, operating, procuring, or assuring a DPI/AI system and need to turn a governance concern into a testable implementation change.

## 1. Start from a gap, not from a template

A valid gap records the observed condition, evidence, required capability, remediation coverage, expected artifacts, closure evidence, and lifecycle status.

```bash
dpi-lab gaps-validate path/to/governance-gaps.yaml --summary
```

Do not treat a low score alone as a remediation requirement. Confirm the evidence and normalize the missing capability first.

## 2. Resolve the capability

Use the companion Artifacts repository remediation registry. A capability may be:

- **standardized** — reusable implementation assets exist;
- **partial** — useful assets exist but the capability is not fully covered;
- **none** — the repeated gap should drive new artifact development.

A mapping is a recommendation, not a transfer of legal, programme, procurement, or deployment authority.

## 3. Instantiate, do not merely adopt

Copying a template does not close a gap. Instantiate the artifact against the actual deployment:

- identify accountable actors and authorities;
- bind scope and lifecycle;
- configure runtime controls;
- define evidence production;
- define adverse and failure paths;
- define redress and remedy where effects can be adverse.

## 4. Test negative paths

At minimum, test the conditions that should prevent or reverse an effect: missing authority, exceeded scope, stale evidence, revocation, failed correlation, unavailable redress, and other case-specific failure states.

## 5. Produce closure evidence

Closure is evidence-bearing. Store the required manifests, hashes, control-to-evidence mappings, authorization records, appeal tests, or other evidence named by the gap record.

## 6. Re-evaluate

A gap moves to `closed` only when the acceptance criteria are satisfied and the supporting evidence can be verified. The re-evaluation should preserve the before/after result so improvement is measurable.

## Operator definition of done

A governance gap is not done when a document has been written. It is done when:

1. the missing capability exists in the deployment;
2. required adverse paths have been exercised;
3. evidence is preserved and integrity-bound;
4. the acceptance criteria pass; and
5. re-evaluation records the improved state.

# TRACE Executable Governance Evaluation Preview

TRACE is being extended from deterministic policy-paper review into an experimental executable-governance evaluation capability.

This preview does **not** transfer normative authority from upstream policy, law, specifications, operators, or institutions to the Lab. It provides a repository-owned method for making governance propositions testable and evidence-bearing.

## Evaluation pipeline

```text
source proposition
  -> governance claims
  -> authority and delegation
  -> actors and governed actions
  -> runtime decision points
  -> evidence requirements
  -> revocation and redress
  -> adversarial scenarios
  -> assurance evidence
```

## Required evaluation artifacts

An executable-governance evaluation directory contains:

- `governance-model.yaml` — authority, delegation, actions, decision points, evidence, revocation, redress, and assurance claims.
- `scenarios.yaml` — positive and negative vectors with deterministic expected outcomes.
- `evidence-manifest.json` — generated SHA-256 bindings for the validated evaluation inputs.

The evidence manifest is generated rather than hand-authored so validation can detect later mutation of the evaluated inputs.

## Authority discipline

Every governance claim identifies one of three authority classes:

- `upstream` — a proposition attributed to an external authoritative source. TRACE records but does not originate the authority.
- `evaluator` — an analytical or methodological assertion owned by this evaluation.
- `inferred` — an explicit inference that must not be represented as upstream normative content.

Delegation records must reference declared authority. Runtime decision points must reference declared actions and evidence requirements. These checks are structural assurance controls, not legal determinations.

## Required adversarial coverage

Any evaluation containing delegation must include negative vectors covering at least:

- scope violation;
- revocation or expiry;
- missing, stale, or uncorrelated evidence; and
- unavailable or ineffective redress.

The preview deliberately treats a technically valid transaction with no redress path as a governance failure rather than a successful execution.

## CLI

Validate an evaluation:

```bash
dpi-lab governance-validate case-studies/executable-governance-entitlement-agent
```

Generate the evidence manifest:

```bash
dpi-lab governance-manifest case-studies/executable-governance-entitlement-agent
```

Validate the evaluation and verify the generated hashes:

```bash
dpi-lab governance-validate case-studies/executable-governance-entitlement-agent --verify-manifest
```

## Worked case

`case-studies/executable-governance-entitlement-agent/` models a delegated service agent that may initiate a public-service entitlement payment only after current eligibility evidence, bounded delegated authority, and runtime authorization are all present.

The case tests scope escalation, pre-effect revocation, missing/stale evidence, effect-to-authorization correlation, and redress availability. It is intentionally experimental and jurisdiction-neutral.

## Portfolio interoperability

The preview is designed for later machine-readable mappings to portfolio components without creating hidden normative dependencies:

| Component | Intended relationship | Authority effect |
| --- | --- | --- |
| TSMM | semantic model mapping | none |
| GAAM | authority/delegation/assurance mapping | none |
| TIS | portable evidence representation | none |
| RAHP | adversarial pressure-testing input | none |
| Trust Protocol Interop Lab | executable cross-system evaluation | none |

Future mappings must state relationship type and normative status explicitly. `maps-to` or `informs` must never be interpreted as `depends-on`, conformance, endorsement, or transfer of authority.

## Preview maturity gate

The capability remains **Experimental** until multiple independently structured worked cases demonstrate:

1. deterministic validation;
2. repeatable negative-vector execution;
3. stable schema semantics;
4. evidence-manifest integrity;
5. documented authority boundaries; and
6. no regression to the existing TRACE paper-review workflow.

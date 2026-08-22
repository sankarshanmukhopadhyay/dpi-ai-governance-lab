# TRACE Operator Improvement Loop

## Mission

The DPI AI Governance Lab exists to make evaluation useful to people who design, procure, implement, operate, assure, and improve DPI-AI systems.

The core loop is:

```text
publication or system proposition
  -> TRACE evaluation
  -> evidence-backed governance gaps
  -> normalized capability requirements
  -> standardized remediation artifacts
  -> implementation
  -> test and assurance evidence
  -> gap closure or residual risk
  -> re-evaluation
```

Sophistication is valuable when it improves one or more stages of this loop. New frameworks, schemas, mappings, threat models, and executable-governance capabilities should therefore identify the operator outcome they enable.

## Repository responsibilities

### Lab

The Lab owns the evaluation side of the loop:

- source ingestion and evidence preservation;
- repeatable TRACE evaluation;
- gap identification and normalization;
- gap severity and confidence;
- capability requirements;
- remediation requirements;
- closure criteria;
- re-evaluation and improvement measurement.

The Lab does not acquire jurisdictional, institutional, or upstream specification authority by evaluating a source.

### Governance Artifacts

The companion `dpi-ai-governance-artifacts` repository owns reusable remediation assets:

- controls;
- schemas;
- templates;
- playbooks;
- test vectors;
- implementation profiles;
- evidence requirements; and
- conformance mechanisms.

A reference from the Lab to an artifact is a remediation mapping. It does not transfer normative authority unless an external governance arrangement explicitly says so.

## Canonical handoff

The machine-readable handoff from evaluation to implementation is `governance-gaps.yaml`, validated by `schemas/findings/governance-gaps.schema.json`.

Each material gap records:

1. what condition was observed;
2. the evidence supporting the finding;
3. the capability the deployment needs;
4. remediation requirements;
5. known standardized artifacts, if any;
6. evidence required for closure; and
7. current lifecycle status.

This makes a TRACE finding actionable without forcing an operator to reinterpret a narrative report.

## Operator states

Gap lifecycle states are intentionally implementation-oriented:

- `open` — material gap identified; remediation may not yet exist;
- `remediation_available` — partial or standardized remediation can be selected;
- `implementation_pending` — remediation has been selected but not evidenced in deployment;
- `verification_pending` — implementation evidence exists and awaits assurance;
- `closed` — acceptance criteria have been met with evidence;
- `accepted_risk` — accountable authority has explicitly retained the residual risk.

`closed` means evidence-backed closure within the evaluation scope. It is not a legal compliance or certification claim.

## Programme metrics

The workbench reports metrics that measure utility rather than repository volume:

- total material gaps;
- gaps with partial remediation coverage;
- gaps with standardized remediation coverage;
- gaps with no known remediation artifact;
- closed gaps;
- artifact coverage ratio;
- standardized remediation ratio; and
- closure ratio.

The primary programme objective is to improve these ratios across independently evaluated publications and deployments without weakening evidence quality or authority boundaries.

## PR mission gate

Every substantive feature PR should state:

```markdown
## Mission contribution

Stage improved: <Evaluate | Find | Normalize | Remediate | Implement | Verify | Re-evaluate>

Before:
<operator or implementer limitation>

After:
<new capability or reduced burden>

Evidence:
<tests, fixtures, mappings, or executed cases proving the improvement>
```

A technically impressive feature that cannot identify a contribution to this loop should normally be deprioritized or reframed.

## Definition of useful

A gap is useful to an implementer when they can determine, without reconstructing the evaluator's reasoning:

- what is missing or unsafe;
- why the finding was made;
- what capability is required;
- which reusable artifacts can help;
- what must be instantiated or changed;
- what tests should pass; and
- what evidence demonstrates closure.

This is the standard against which the Lab's future development should be judged.

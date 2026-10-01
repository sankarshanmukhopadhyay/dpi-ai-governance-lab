---
layout: default
title: Assurance continuity
nav_order: 9
---

# Assurance continuity

A capability assessment is a historical statement about an implementation, evidence set, conformance profile and evaluation time. Its recorded result does not change when the world changes later.

Continuing reliance is therefore represented by a **separate continuity result**.

```text
historical capability assessment
        +
observed change evidence
        +
versioned profile continuity rules
        ↓
present continuity state
```

## State model

- `valid`: no evidenced material change requires a different state;
- `superseded`: a later verified assessment explicitly replaces the prior assessment for current reliance;
- `reassessment_required`: a known material change falls under a profile rule requiring fresh evaluation;
- `invalidated`: a known evidenced change revokes or contradicts a basis required for present reliance;
- `indeterminate`: a change is observed but cannot be classified, lacks sufficient evidence, or cannot be resolved against the declared contract.

The original assessment remains immutable. For example, an assessment that passed on 1 October remains a historical PASS even if delegation is revoked on 2 October. Its **current continuity state** becomes `invalidated`.

## Deterministic precedence

When multiple conditions are present, the validator applies:

```text
verified explicit supersession
  -> known invalidating event
  -> unknown / insufficiently evidenced event
  -> known reassessment-required event
  -> valid
```

This avoids treating uncertainty as continued validity.

## Cross-repository responsibility

Artifacts owns the reusable mapping from classified change types to technical effects such as `reassessment_required` or `invalidates`.

The Lab owns the derived continuity determination from:

- a prior immutable assessment;
- an immutable Artifacts continuity profile baseline;
- observed change events;
- evidence supporting those events.

Operators and adopting institutions remain responsible for detecting real-world changes and for the legal, policy and operational consequences of those changes.

## Independent fixture

The existing public-benefit fixture now proves:

| Event | Continuity state |
| --- | --- |
| no material change evidenced | `valid` |
| delegation revoked | `invalidated` |
| implementation changed | `reassessment_required` |
| later assessment replaces prior | `superseded` |
| unclassified change | `indeterminate` |
| asserted change without evidence | `indeterminate` |

Machine-verifiable surfaces:

- `schemas/assurance/assessment-continuity.schema.json`
- `tools/validate_assessment_continuity.py`
- `case-studies/public-benefit-assurance-handoff/continuity-*.yaml`

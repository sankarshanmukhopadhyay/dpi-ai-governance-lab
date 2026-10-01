---
layout: default
title: Capability assurance handoff
nav_order: 8
---

# Capability assurance handoff

TRACE can identify a governance gap and normalize the required `CAP-*`. The Artifacts repository can provide a versioned capability conformance profile. This handoff defines how implementation evidence returns to the Lab without giving either repository deployment authority.

```text
GAP-*
  -> required CAP-*
  -> versioned Artifacts profile
  -> implementation evidence
  -> requirement results
  -> portable capability assessment
  -> scoped TRACE re-evaluation
```

## Determination semantics

A capability assessment supports:

- `pass`: every mandatory requirement passes and every required evidence class is present;
- `fail`: at least one mandatory requirement fails;
- `partial`: mandatory requirements pass but a non-mandatory requirement fails;
- `indeterminate`: required evidence is missing or a mandatory requirement cannot be evaluated;
- `not_evaluated`: the implementation has not yet been assessed.

Missing evidence never becomes PASS.

## Continuity after assessment

The assessment result is historical evidence and is not rewritten after later events. Present reliance after authority, policy, implementation, evidence, or profile change is represented separately through an assessment-continuity result.

See [Assurance continuity](assurance-continuity.md) for the lifecycle state model and deterministic change handling.

## Version binding

Every assessment identifies the Artifacts repository, immutable commit, interface version, capability ID and profile ID used for evaluation. This allows a future reviewer to reconstruct which technical contract governed the assessment.

## Independent fixture

`case-studies/public-benefit-assurance-handoff/` is deliberately separate from the Digital Statecraft corpus. It exercises the reusable handoff against a synthetic public-benefit eligibility service.

The fixture proves three cases:

1. complete evidence and passing mandatory requirements -> PASS;
2. required evidence omitted -> INDETERMINATE;
3. mandatory requirement failure -> FAIL.

## Authority boundary

The Lab produces a derived technical assessment within the declared fixture or deployment scope. It does not certify a production service, create legal compliance, authorize a consequential decision, or override the adopting institution's accountable authority.

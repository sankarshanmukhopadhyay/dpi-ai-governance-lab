---
layout: default
title: Public benefit assurance handoff
nav_order: 8
---

# Public benefit assurance handoff

This synthetic fixture proves that the Lab can consume version-bound capability conformance semantics without relying on the Digital Statecraft corpus or capability-specific evaluator code.

The service proposition is intentionally small: a public-benefit eligibility service uses delegated automation to authorize a consequential eligibility effect. A later correction to a source fact must propagate through the eligibility decision and benefit effect.

The fixture is bound to Artifacts commit `9dfc73e451a56283211674b5c874ae382ead53f8`, which introduced capability conformance interface 1.0 for bounded delegation and correction propagation.

## Evidence cases

- `assessment-pass.yaml`: bounded-delegation requirements pass with all required evidence classes present.
- `assessment-missing-evidence.yaml`: a required evidence class is absent, so the result is `indeterminate`.
- `assessment-failed-requirement.yaml`: a mandatory negative-path requirement fails, so the result is `fail`.
- `assessment-correction-pass.yaml`: correction propagation passes with source order, dependency, execution, recomputation and partial-failure evidence.

## Continuity cases

The original `assessment-pass.yaml` remains unchanged and continues to represent the historical assessment made on 1 October 2026. Separate continuity fixtures demonstrate present reliance after later events:

- no material change -> `valid`;
- delegation revocation -> `invalidated`;
- implementation change -> `reassessment_required`;
- later assessment -> `superseded`;
- unclassified or unsupported change -> `indeterminate`.

The continuity rules are pinned to Artifacts commit `2ee7b803c1ee8a9000e329e9ee25262b1be32fa8`.

## Assurance boundary

These are synthetic technical assessments. They do not certify a production service, establish legal compliance, or determine who has real-world authority to delegate, decide, correct, compensate, or close a case.

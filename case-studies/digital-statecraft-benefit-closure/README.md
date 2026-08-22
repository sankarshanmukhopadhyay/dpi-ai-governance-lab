---
layout: default
title: Digital Statecraft benefit closure
nav_order: 9
---

# Digital Statecraft benefit closure

This synthetic, jurisdiction-neutral public-benefit fixture demonstrates the complete improvement loop using all six recurring capability classes found across the first-wave Digital Statecraft corpus.

It does **not** claim that a publication has been fixed, that a production deployment conforms, or that the example policy is legally appropriate.

## Architecture

```mermaid
flowchart LR
    A[Employment registry\nupstream evidence] --> B[Admissibility gate]
    B --> C[Eligibility agent\nbounded delegation]
    C --> D[Risk inference\ntrace + version]
    D --> E[Authorized rulebook]
    E --> F[Decision receipt]
    F --> G[Runtime authorization]
    G --> H[Payment effect]
    F --> I[Appeals office]
    I --> J[Correction order]
    J --> K[Recompute decision]
    J --> L[Compensate effect]
    K --> M[Closure evidence]
    L --> M
```

## Authority and decision sequence

```mermaid
sequenceDiagram
    participant R as Employment registry
    participant B as Benefits agency
    participant A as Eligibility agent
    participant M as Inference service
    participant P as Payment service
    participant O as Appeals office

    R->>B: authentic income evidence
    B->>B: admissibility decision
    B->>A: bounded delegated authority
    A->>M: evaluate risk input
    M-->>A: output + inference trace
    A->>B: rule-bound decision proposal
    B->>B: runtime authorization + decision receipt
    B->>P: authorized payment effect
    alt adverse/disputed case
        B->>O: appeal evidence
        O->>R: authorize fact correction
        O->>B: correction order / recompute
        O->>P: remedy or compensation
    end
```

## Capabilities exercised

| Capability | Fixture evidence |
| --- | --- |
| `CAP-AUTHORITY-BOUNDED-DELEGATION` | scoped delegation + authorization + scope/revocation negatives |
| `CAP-INTERINSTITUTIONAL-ADMISSIBILITY` | upstream reliance profile + authentic-but-inadmissible negative |
| `CAP-INFERENCE-TRACEABILITY` | immutable model/version/input/threshold trace + mutation negatives |
| `CAP-REDRESS-APPEAL` | appeals authority + successful disposition + unavailable-redress negative |
| `CAP-CORRECTION-PROPAGATION` | correction order + recomputation/compensation + partial-failure negative |
| `CAP-EVIDENCE-CLOSURE` | effect correlation + capability/acceptance evidence + broken-correlation negative |

## Before and after

The historical Lab baseline against Artifacts registry 0.2.0 recorded **10 of 19** gaps with standardized remediation (52.63%). The artifact development sequence subsequently standardized the three missing recurring capabilities. This fixture then demonstrates that the resulting six-capability package can be instantiated and adversarially exercised together.

The before/after claim is scoped carefully:

```text
historical publication-gap coverage: 52.63%
        ↓
evidence-derived artifact development
        ↓
current first-wave capability mapping: 100%
        ↓
synthetic selected-capability closure: 6/6 pass
```

The publication-level closure rate remains zero because no Digital Statecraft essay is itself a deployment.

## Negative-path evidence

The fixture denies or fails as expected for:

- delegated action outside scope;
- revoked delegation;
- authentic but inadmissible evidence;
- inference model version mismatch;
- decision-relevant threshold mismatch;
- unavailable redress;
- partial mandatory correction propagation;
- broken effect-to-authorization correlation.

Run:

```bash
python tools/validate_digital_statecraft_benefit_closure.py
```

## Evidence files

- [`system-profile.yaml`](system-profile.yaml)
- [`implementation-evidence.yaml`](implementation-evidence.yaml)
- [`adversarial-scenarios.yaml`](adversarial-scenarios.yaml)
- [`closure-evidence.yaml`](closure-evidence.yaml)

## Assurance boundary

The fixture proves only that these repository contracts can be composed and deterministically tested in the declared synthetic scenario. Real deployment closure would require real authority records, implementation evidence, cryptographic integrity, operating logs, affected-person redress tests, and jurisdiction-specific review.

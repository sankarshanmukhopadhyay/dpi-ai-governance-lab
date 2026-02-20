# Sovereignty Assurance Model (SAM)
## Turning posture (C/S/D) into proof-carrying governance

**Purpose.** The source paper introduces *Control / Steer / Depend (CSD)* as strategic postures across the AI stack. This module converts posture into **attestable evidence**: what must exist (artifacts), what must be observable (runtime proofs), and what must be testable (conformance checks).

> **Core principle:** *Sovereignty is not declared. It is continuously evidenced.*

---

## SAM control ID taxonomy

Control IDs are structured as:

`SAI-<LAYER>-<DOMAIN>-<NN>`

- `LAYER`: `CMP` compute, `ENG` energy, `DAT` data, `MOD` models, `APP` applications, `SKL` talent/skills, `GOV` governance
- `DOMAIN`: `RES` resilience, `AUD` auditability, `INT` interoperability, `JUR` jurisdiction, `SEC` security, `RED` redress, `CAP` capacity
- `NN`: sequential number

Example: `SAI-CMP-RES-01`

---

## SAM baseline: posture → required evidence

### Compute infrastructure

**Control posture (Control / Steer / Depend)** determines the minimum evidence bar.

| Posture | Required institutional artifacts | Required runtime proofs | Minimum tests |
|---|---|---|---|
| Control | Domestic hosting policy; sovereign compute inventory; outage playbooks | Inference continuity metrics; failover traces; capacity reservation logs | Annual failover drill; quarterly capacity audit |
| Steer | Procurement clauses for portability; audit-rights schedule; multi-cloud policy | Workload migration logs; provider performance telemetry | Contract conformance review; portability test |
| Depend | Multi-year access agreements; non-interruption clause; exit plan | SLA adherence logs; provider policy change logs | Vendor risk review; exit tabletop |

**Controls**
- `SAI-CMP-RES-01` Maintain domestic inference capacity for mission-critical services.
- `SAI-CMP-AUD-02` Record and retain workload placement + failover execution evidence.
- `SAI-CMP-INT-03` Demonstrate portability across at least 2 compliant runtimes/providers.
- `SAI-CMP-SEC-04` Maintain secure enclave / HSM-backed key custody for sovereign workloads.

---

### Energy

| Posture | Required institutional artifacts | Required runtime proofs | Minimum tests |
|---|---|---|---|
| Control | AI energy zones policy; firm capacity planning; PPAs | Grid reliability metrics; compute energy intensity reports | Annual peak-load simulation |
| Steer | Green-compute standard; reporting obligations | Vendor energy reporting; utilisation evidence | Quarterly reporting compliance |
| Depend | Import/region reliance plan; contingency contracts | Stress telemetry; curtailment traces | Cross-border disruption tabletop |

**Controls**
- `SAI-ENG-RES-01` Integrate AI demand forecasts into grid planning.
- `SAI-ENG-AUD-02` Require transparent energy + emissions reporting for AI infrastructure.
- `SAI-ENG-SEC-03` Maintain continuity plans for compute under grid stress.

---

### Data

| Posture | Required institutional artifacts | Required runtime proofs | Minimum tests |
|---|---|---|---|
| Control | Data trust charter; access policy; consent/legal basis registry | Access logs; privacy risk metrics; provenance attestations | Annual privacy audit |
| Steer | Open standards for data formats; data-sharing agreements | Dataset versioning + lineage logs | Portability/lineage test |
| Depend | Vendor data governance contract; extraction rights | Export logs; deletion proofs | Exit data extraction drill |

**Controls**
- `SAI-DAT-JUR-01` Enforce domestic jurisdiction for sensitive datasets.
- `SAI-DAT-AUD-02` Maintain lineage + provenance for training and fine-tuning data.
- `SAI-DAT-SEC-03` Demonstrate privacy-preserving processing for protected domains.

---

### Models

| Posture | Required institutional artifacts | Required runtime proofs | Minimum tests |
|---|---|---|---|
| Control | Model governance board; model registry; release gates | Versioned eval results; rollback traces | Pre-release evaluation suite |
| Steer | Audit rights; change-notice requirements; model card requirements | Monitoring logs; drift alerts | Quarterly evaluation |
| Depend | Provider terms; fallback models; exit/escrow plan | SLA/latency logs; incident traces | Vendor policy-change tabletop |

**Controls**
- `SAI-MOD-AUD-01` Maintain continuous evaluation, including drift detection.
- `SAI-MOD-RES-02` Ensure rollback and fallback capability within defined RTO/RPO.
- `SAI-MOD-SEC-03` Validate supply chain integrity for weights and dependencies.

---

### Applications

| Posture | Required institutional artifacts | Required runtime proofs | Minimum tests |
|---|---|---|---|
| Control | DPI integration architecture; service governance; accountability roles | End-to-end traceability; redress triggers | Incident drill |
| Steer | Procurement standards; API requirements; portability guarantees | Interface conformance logs; switching tests | Semi-annual portability test |
| Depend | Vendor governance; exit clauses; local operator training | Audit logs; escalation traces | Exit tabletop |

**Controls**
- `SAI-APP-RED-01` Implement a redress mechanism with trace-backed case handling.
- `SAI-APP-AUD-02` Maintain decision trace records for high-impact workflows.
- `SAI-APP-INT-03` Require open APIs and vendor-neutral orchestration.

---

### Talent and skills

**Controls**
- `SAI-SKL-CAP-01` Establish public-sector technical career tracks (retain + rotate).
- `SAI-SKL-CAP-02` Define minimum AI literacy for procurement + oversight roles.
- `SAI-SKL-AUD-03` Track workforce capability coverage against system risk tiers.

---

### Governance

**Controls**
- `SAI-GOV-AUD-01` Maintain an AI system inventory with tiering, owners, and controls.
- `SAI-GOV-SEC-02` Adopt incident taxonomy + reporting SLAs.
- `SAI-GOV-RED-03` Maintain appeals + redress SLAs for citizen-impacting systems.
- `SAI-GOV-INT-04` Participate in standards alignment to avoid “interop isolation”.

---

## Conformance and evidence pack

A compliant implementation SHOULD maintain an evidence pack containing:
- posture declaration (`posture-declaration.json`)
- SARI baseline + quarterly updates
- control artifacts (policies, contracts, charters)
- runtime proofs (logs, traces, evaluation outputs)
- drill records (tabletops, failover tests)
- redress/appeals case logs (with privacy protections)

See:
- `schemas/sovereignty-age-of-ai-2026/posture-declaration.schema.json`
- `sovereignty-readiness-index.md`
- `ai-infrastructure-resilience-playbook.md`

# DPI-Linked Sovereign AI Readiness Index (SARI)
## A measurable instrument for agency, resilience, and exit leverage

**Purpose.** The source paper frames sovereignty as *agency and choice* under interdependence. SARI translates that into a repeatable measurement system that can be:
- self-assessed by governments,
- benchmarked across programs,
- tracked as a maturity curve.

SARI is designed to align with DPI doctrine: shared rails, reusable registries, auditable workflows, and strong institutional accountability.

---

## Scoring approach

- **Scale:** 0–5 per dimension (0 = absent, 5 = institutionalized + routinely evidenced)
- **Cadence:** baseline + quarterly updates
- **Output:** a portfolio heatmap and a prioritized backlog

### Dimensions (per AI stack layer)
1. **Fallback capacity** (continuity under disruption)
2. **Negotiated interdependence quality** (contracts, rights, exit provisions)
3. **Runtime auditability** (logs, traces, evaluation observability)
4. **Representation adequacy** (data/language/context coverage)
5. **Energy–compute resilience coupling** (energy planning aligned to compute)
6. **Public-sector absorption capacity** (skills, procurement, delivery capability)

---

## Scoring rubric (0–5)

### 0 — None
No defined artifacts, no operational evidence.

### 1 — Ad hoc
Point solutions exist; inconsistent ownership; evidence is not retained.

### 2 — Defined
Policies exist; minimal standardization; evidence retention is partial.

### 3 — Managed
Controls are implemented programmatically; audits occur; gaps are tracked.

### 4 — Integrated
Cross-government alignment; procurement + runtime controls are consistent; drills and evaluations are routine.

### 5 — Institutionalized
Metrics are automated; controls are continuously verified; postures can be renegotiated quickly based on evidence and changing risk.

---

## SARI outputs

### A) Layer heatmap
Compute / Energy / Data / Models / Applications / Talent / Governance × Dimensions

### B) “Sovereignty backlog”
Each low score becomes an actionable work item, linked to SAM control IDs.

### C) Portfolio narrative
A short policy narrative explaining:
- where the state seeks Control,
- where it will Steer,
- where it will Depend (and how dependence is managed).

---

## Recommended weighting (opinionated)
Sovereignty fails at runtime, so weight auditability + fallback highest.

- Runtime auditability: **25%**
- Fallback capacity: **20%**
- Negotiated interdependence quality: **15%**
- Interoperability/exit leverage: **15%**
- Representation adequacy: **10%**
- Energy–compute resilience coupling: **10%**
- Public-sector absorption capacity: **5%**

---

## Machine-readable format
See:
- `schemas/sovereignty-age-of-ai-2026/sari-assessment.schema.json`
- `schemas/sovereignty-age-of-ai-2026/sari-assessment.example.yaml`

Template:
- `templates/sari-assessment-template.yaml`

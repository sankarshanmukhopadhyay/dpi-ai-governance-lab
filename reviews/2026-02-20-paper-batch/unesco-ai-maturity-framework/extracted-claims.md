# Paper analysis — UNESCO AI Maturity Framework: A self-positioning guide for public administrations

## 1. Architectural Primitives Extracted

- **Identity rails:** Not a focus; assumes public administration context but does not specify identity/delegation controls.
- **Data exchange layer:** Treated as organisational capability (policies, governance bodies) rather than operational exchange primitives.
- **AI capability layer:** Focuses on *maturity stages* (self-positioning) more than system architecture.
- **Governance assumptions:** Strong on institutional readiness (leadership, ethics, skills, procurement), weak on runtime control surfaces.

## 2. Institutional Risk Surfaces

| Risk | Failure Mode | Likelihood | Impact | Priority |
|------|-------------|------------|--------|----------|
| Maturity theatre | Score improves while real systems remain un-auditable and un-contestable | High | High | P1 |
| Procurement-led architecture | “Capability” purchased as black boxes; accountability outsourced | High | High | P1 |
| Missing tier triggers | Administrations deploy Tier 2/3 systems using Tier 1 governance practices | Medium | High | P1 |
| Weak redress operationalisation | Rights-affecting systems deployed without SLAs, appeal hooks, remedy taxonomy | Medium | High | P2 |
| Data stewardship gaps | Data sharing expands faster than consent/audit/secondary-use controls | Medium | High | P2 |

## 3. Risk-to-Tier Mapping

Recommendation: integrate the lab’s Tier 0–3 model into the maturity guide:

- Maturity should be scored **per tier** (Tier 0 readiness ≠ Tier 3 readiness).
- Gate Tier 2/3 deployments on mandatory artifacts (deployment dossier, evaluation evidence, redress model).

## 4. Governance Binding

Suggested “maturity-to-controls” binding:

- For each maturity dimension, specify **control objectives** and **evidence** (logs, attestations, test reports).
- Define explicit **RACI ownership** for model updates, incident response, and complaint handling.
- Require “public accountability surfaces”: model registry entries, policy declarations, and audit summaries.

## 5. Standards Alignment

- **NIST AI RMF / OECD / ISO 42001:** this paper is a helpful *governance readiness wrapper*, but requires a technical control plane to be actionable.
- **DPI building blocks:** missing; would benefit from a DPI mapping annex (identity, registries, data exchange, audit, redress).

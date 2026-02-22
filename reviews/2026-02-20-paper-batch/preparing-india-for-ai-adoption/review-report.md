# Paper review report — Preparing India for AI Adoption: Challenges and Solutions

## 1. Executive framing
- **Thesis:** India can capture AI value if it closes gaps in infrastructure, skills, governance and ethics.
- **What the paper gets right:** Names the real blockers (capacity, curricula, regulation, ethics) and treats adoption as a system problem, not just an R&D problem.
- **What it misses:** A DPI-grade operating model: workflow tiering, runtime decision rights, auditability, and redress plumbing. Without these, “adoption” becomes procurement + hope.

## 2. Use-case and tier mapping
- **Candidate use-cases:**
  - Citizen information assistants for schemes/services (Tier 0).
  - Staff copilots for drafting, summarisation, triage (Tier 1).
  - Fraud/risk scoring and eligibility recommendation (Tier 2).
  - Automated approvals/denials, enforcement triggers (Tier 3 — should be exceptional).
- **Tier mapping + justification:**
  - The paper should explicitly state that anything affecting eligibility/entitlements/enforcement is Tier 2+ and demands contestability and audit trails.

## 3. Accountability and runtime governance
- Accountability chain present? **N**
- Escalation triggers present? **N**
- Kill switch / rollback present? **N**

## 4. Data exchange governance
- Stewardship model: **Implied** (policy-level), not operationalised.
- Auditability: **Not specified** (no logs/evidence requirements).
- Secondary use controls: **Not specified**.

## 5. Conformance profile alignment
- Profile Basic: **Partial** (general governance intent).
- Profile Decision Support: **Missing** (no Tier 2 requirements).
- Profile Automated Action: **Missing** (no Tier 3 gating).

## 6. Redress and remedy
- Contestability: **Mentioned as ethics concern**, not implemented.
- SLAs: **Absent**.
- Remedies: **Absent** (no remedy taxonomy, no escalation owners).

## 7. Sovereignty / compute dependence
- Key dependencies: External models/compute likely; not analysed in detail.
- Resilience posture: **Unspecified**.

## 8. Required artifacts missing
- Missing dossier elements: tier declaration, use-case scoping, model/data provenance, human-in-the-loop gates.
- Missing evaluation elements: benchmark minimums, bias/fairness tests, drift monitoring.
- Missing governance plumbing: RACI, incident escalation model, grievance SLAs, kill switch/rollback.

## 9. Recommendations (minimal viable upgrades)
1. Add a **tiering section** (Tier 0–3) and classify the paper’s use-cases.
2. Introduce a **contestable decision record** requirement for Tier 2.
3. Define a minimal **runtime accountability chain** (owner, operator, auditor, ombuds).
4. Add **procurement guardrails**: audit rights, interoperability, logging, data-use constraints.
5. Attach a one-page **deployment dossier checklist** for public-sector deployments.

---

## Addendum (from rolling 2026 pack)

# Review report (draft)

This review is produced using the DPI AI Governance Lab artifacts.

## Key gap closure targets

- Introduce **risk-tier binding** for DPI-scale deployments
- Define **runtime accountability and escalation plumbing**
- Require a deployable **AI Deployment Dossier** for Tier 2–3
- Specify **data exchange governance** beyond general stewardship language
- Surface **compute dependency** as leverage risk, not only capacity

(See `/artifacts/*` for the normative machinery.)

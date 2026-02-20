# Paper analysis — Preparing India for AI Adoption: Challenges and Solutions

## 1. Architectural Primitives Extracted

- **Identity rails:** Assumed (Aadhaar / national identity ecosystems implied), but not specified as programmable rails. No explicit delegation, consent receipts, or verifier-grade provenance.
- **Data exchange layer:** Discusses “data availability” and governance at a policy level; no concrete exchange primitives (data spaces, schemas, trust registries, audit logs).
- **AI capability layer:** Frames AI as sectoral adoption (health, farming, education, government). Treats models as “capability” rather than components in workflows (no inference boundary conditions, no guardrail blocks).
- **Governance assumptions:** High-level ethics + regulation + skilling. Implicit assumption that “more policy + more talent” yields safe scale, without specifying runtime decision rights.

## 2. Institutional Risk Surfaces

| Risk | Failure Mode | Likelihood | Impact | Priority |
|------|-------------|------------|--------|----------|
| Governance-by-aspiration | Policies exist but no operational control plane; systems drift into Tier 2/3 behavior by accident | High | High | P1 |
| Data governance thin-slicing | “Data access” expands without stewardship/audit plumbing; secondary use becomes default | Medium | High | P1 |
| Vendor capture | Adoption playbooks become procurement of opaque stacks; lock-in and audit debt | High | Medium | P2 |
| Equity and language gaps | Benefits concentrate in English-first and urban contexts | High | Medium | P2 |
| Accountability diffusion | Harms become “no owner”; complaints loop into bureaucracy | Medium | High | P1 |

## 3. Risk-to-Tier Mapping

- The paper implicitly spans **Tier 0 → Tier 3**, but never classifies workflows.
- Minimal viable tier rule-set to add:
  - **Tier 0:** informational assistants (policy FAQs, guidance) with no effect on eligibility/enforcement.
  - **Tier 1:** staff copilots for drafting, triage, summarisation; **human decision required**.
  - **Tier 2:** eligibility/entitlement/enforcement recommendations; requires **contestable record + audit trail + explanation**.
  - **Tier 3:** any automated approvals/denials/sanctions; **prohibited-by-default** unless strict conditions (kill switch, rollback, independent oversight).

## 4. Governance Binding

Map missing in paper; recommend adding a binding table:

- **Controller obligations:** declare tier; publish decision rights; maintain model cards + dataset provenance; keep incident register.
- **Block provider obligations:** signed outputs for machine-consumed responses; versioned policies; evaluation minimums; drift monitoring.
- **DPI operator controls:** identity-bound access, workload segregation, audit logging, rate limits, jurisdictional controls.
- **Escalation pathways:** Tier 2/3 must have escalation triggers (appeal, override, suspension) and named RACI owners.

## 5. Standards Alignment

- **NIST AI RMF:** “govern + map + measure + manage” intent is present; operational evidence paths are missing.
- **OECD AI Principles:** fairness/transparency themes present, but no system-level enforcement mechanisms.
- **ISO 42001:** management-system framing implied; no control objectives or evidence requirements.
- **DPI building blocks:** referenced conceptually (India’s digital ecosystem) but not formalised as interoperable blocks.

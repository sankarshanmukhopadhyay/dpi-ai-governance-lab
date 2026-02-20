# Paper review report — Vision Paper: DPI-AI Framework 2026 (CDPI)

## 1. Executive framing
- **Thesis:** Treat AI as composable infrastructure inside DPI: callable AI blocks + workflow orchestration + safeguards as first-class modules.
- **What the paper gets right:** The decomposition is excellent. “Blocks + workflows + safeguards” is the cleanest path to testable interoperability and governance-by-construction.
- **What it misses:** Hard tier triggers, evidence requirements, and a strict posture on agent authority (preventing Tier drift).

## 2. Use-case and tier mapping
- **Candidate use-cases:**
  - Policy/service discovery assistants (Tier 0).
  - Caseworker copilots for drafting/triage (Tier 1).
  - Eligibility recommendation and prioritisation (Tier 2).
  - Automated approvals/denials and enforcement (Tier 3).
- **Tier mapping + justification:**
  - Embed tier declarations directly into workflow YAML. Treat “public agents” as Tier 1 by default; Tier 2/3 requires explicit gating.

## 3. Accountability and runtime governance
- Accountability chain present? **Partial** (oversight intent, not a full RACI).
- Escalation triggers present? **Partial** (mentions oversight/inspection; needs runtime triggers).
- Kill switch / rollback present? **Partial** (should be mandatory for Tier 2/3 workflows).

## 4. Data exchange governance
- Stewardship model: **Discussed** (governed training data), but needs concrete exchange controls.
- Auditability: **Partially specified**; add required logs, retention, and attestation format.
- Secondary use controls: **Not fully specified**.

## 5. Conformance profile alignment
- Profile Basic: **Strong fit** (block registry, interoperability, baseline controls).
- Profile Decision Support: **Fit with upgrades** (contestable decision records, explanation + audit).
- Profile Automated Action: **Fit only with strict gating** (dossier, audits, rollback, redress).

## 6. Redress and remedy
- Contestability: **Mentioned** (redress appears), but not operational.
- SLAs: **Missing**.
- Remedies: **Missing**.

## 7. Sovereignty / compute dependence
- Key dependencies: Not the primary focus; should include a compute/data locality and exit posture section for public deployments.
- Resilience posture: **Not specified**.

## 8. Required artifacts missing
- Missing dossier elements: agent authority declaration; tier declarations; signed block outputs; policy versioning.
- Missing evaluation elements: minimum test suite per block; drift/observability requirements for workflows.
- Missing governance plumbing: RACI + escalation; redress model; incident SLAs.

## 9. Recommendations (minimal viable upgrades)
1. Add **Tier 0–3** fields and gates in the workflow template (YAML).
2. Require **signed, versioned block responses** when machine-consumed.
3. Define a minimal **block conformance checklist** (schemas, logs, evals, safety tests).
4. Add a **runtime governance section**: kill switch, rollback, drift triggers, suspension rules.
5. Add a **redress bundle** for Tier 2/3: contestability record, SLAs, remedy taxonomy.

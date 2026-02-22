# Paper review report — UNESCO AI Maturity Framework: A self-positioning guide for public administrations

## 1. Executive framing
- **Thesis:** Public administrations can self-assess their readiness to adopt AI across governance, capacity, and operational dimensions.
- **What the paper gets right:** Creates a practical common language for “where are we today?” across institutions that otherwise talk past each other.
- **What it misses:** A DPI-grade control plane. Maturity models without evidence hooks are vulnerable to “maturity theatre”.

## 2. Use-case and tier mapping
- **Candidate use-cases:** The guide is cross-cutting; typical public-sector portfolio includes Tier 0–3 systems.
- **Tier mapping + justification:**
  - Maturity should be assessed **by tier**. Tier 3 readiness is qualitatively different from Tier 1 readiness.

## 3. Accountability and runtime governance
- Accountability chain present? **Partial** (governance structures), not runtime RACI.
- Escalation triggers present? **Weak/implicit**.
- Kill switch / rollback present? **Not explicit**.

## 4. Data exchange governance
- Stewardship model: **Strong at policy level**, weaker at operational controls.
- Auditability: **Not evidence-driven** (no required logs/test outputs).
- Secondary use controls: **Not enforceable as written**.

## 5. Conformance profile alignment
- Profile Basic: **Partial** (readiness framing).
- Profile Decision Support: **Missing** (Tier 2 requires contestability + records).
- Profile Automated Action: **Missing** (Tier 3 gating and prohibition-by-default stance absent).

## 6. Redress and remedy
- Contestability: **Typically referenced**, not specified as a system requirement.
- SLAs: **Absent**.
- Remedies: **Absent**.

## 7. Sovereignty / compute dependence
- Key dependencies: Not central.
- Resilience posture: Not assessed.

## 8. Required artifacts missing
- Missing dossier elements: tier declarations; deployment dossiers; audit-ready logs.
- Missing evaluation elements: benchmark minimums; bias/fairness; drift monitoring.
- Missing governance plumbing: explicit RACI; escalation triggers; redress SLAs.

## 9. Recommendations (minimal viable upgrades)
1. Add a **tiered appendix** mapping maturity questions to Tier 0–3 deployments.
2. Convert maturity items into **control objectives + evidence requirements**.
3. Require a **deployment dossier** for Tier 2/3.
4. Add a **redress and remedy module** (contestability record + SLAs + remedy taxonomy).
5. Introduce a **procurement annex** to prevent black-box adoption.

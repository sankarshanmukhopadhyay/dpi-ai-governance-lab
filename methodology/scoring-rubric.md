# DPI AI Governance Lab — Scoring Rubric (v1.0)

## Status
**Normative.** Reviews MUST use this rubric unless explicitly marked as “Exploratory (non-scored).”

## TRACE (what it stands for)
**TRACE (Trust, Risk, Architecture & Conformance Evaluation)** is the Lab’s named method for assessing DPI–AI systems, programs, and policies.
This rubric is TRACE-compatible and is designed for **auditability** (evidence-linked scores).

See also: `docs/trace/README.md`

## Scoring scale
All dimensions use the 1–5 scale defined in `methodology/scoring-scale.md`.

- **1** = Absent / not addressed
- **2** = Mentioned / conceptual only
- **3** = Partially operationalized
- **4** = Operational with gaps
- **5** = Fully operational and auditable

Reviewers MUST justify each score with evidence pointers.

---

## Rubric dimensions

### D1. Problem definition & scope control
**Evaluation question:** Does the paper define a bounded problem, scope, and non-goals with sufficient clarity to support governance decisions?

**Evidence examples:** explicit scope section, assumptions, limitations, target context, excluded cases.

**High score requires:** clear boundaries that prevent scope creep and allow comparable reviews.

---

### D2. System model & stakeholder model
**Evaluation question:** Does the paper provide a usable system model (components, actors, interfaces) and stakeholder model (who is affected, who controls)?

**Evidence examples:** architecture diagram, actor table, lifecycle model, trust boundaries.

**High score requires:** model supports risk/control reasoning, not just narrative description.

---

### D3. Risk articulation & harm model
**Evaluation question:** Does the paper articulate harms/risks with causal structure (not only a list), including severity/likelihood or comparable prioritization?

**Evidence examples:** threat model, harm taxonomy, causal chain, risk register, misuse cases.

**High score requires:** risk model is specific enough to drive mitigations.

---

### D4. Control strategy & mitigation specificity
**Evaluation question:** Does the paper define controls/mitigations that are actionable and mapped to risks?

**Evidence examples:** control catalog, mitigation mapping table, policy+technical measures, governance process controls.

**High score requires:** mitigations are testable or implementable, not aspirational.

---

### D5. Measurement, evaluation & evidence quality
**Evaluation question:** Does the paper provide measurable evaluation methods and credible evidence for claims?

**Evidence examples:** metrics, experiments, evaluation protocol, datasets, benchmarks, limitations.

**High score requires:** evaluation supports defensible conclusions and acknowledges uncertainty.

---

### D6. Accountability & responsibility assignment
**Evaluation question:** Does the paper specify who is accountable for what, across lifecycle phases, including escalation and exceptions?

**Evidence examples:** RACI-like mapping, governance roles, incident ownership, decision authority.

**High score requires:** accountability is operational (roles + triggers + actions), not rhetorical.

---

### D7. Transparency & explainability of decisions
**Evaluation question:** Are decisions and governance claims explainable to an external stakeholder (auditor, operator, affected party)?

**Evidence examples:** disclosure artifacts, explainability requirements, reporting templates, traceability mechanisms.

**High score requires:** transparency is implemented through artifacts/logs, not promises.

---

### D8. Auditability & traceability mechanisms
**Evaluation question:** Does the paper enable audit (what happened, why, by whom, with what evidence)?

**Evidence examples:** logging/audit trail design, provenance, attestations, decision logs.

**High score requires:** traceability is designed as a system property.

---

### D9. Operational readiness & adoption path
**Evaluation question:** Does the paper provide a credible path from concept to operational deployment?

**Evidence examples:** implementation guidance, adoption phases, integration constraints, cost/latency considerations.

**High score requires:** addresses real-world constraints and adoption friction.

---

### D10. Interoperability & standards alignment
**Evaluation question:** Does the paper align with relevant standards or provide interfaces that allow composability?

**Evidence examples:** mappings to NIST/ISO/ToIP, schema/interface definitions, conformance profiles.

**High score requires:** explicit mappings or interface artifacts, not name-dropping standards.

---

## Optional meta-signals (MAY)
These are not part of the 1–5 rubric but can be recorded in the scorecard for additional signal.

- **Confidence level:** High / Medium / Low (based on evidence clarity)
- **Inference ratio:** Low / Medium / High (how much is inferred vs explicit)
- **Reproducibility risk:** Low / Medium / High (likelihood another reviewer diverges)

---

## Output requirements
The completed rubric MUST be included in `03-scorecard.md` using the scorecard template, and evidence MUST be logged in `04-audit-trail.md`.

## Anti-patterns (MUST avoid)
- Scoring based on writing quality alone
- Rewarding “vision” without operational detail
- Inflating scores due to agreement with the thesis
- Treating “future work” as implemented control

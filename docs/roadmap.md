# Roadmap (Schedule-Free)

This roadmap documents the intended evolution of the DPI AI Governance Lab.
It reflects methodological hardening and research-grade maturity goals.
It does not include delivery timelines.

---

## 1. Methodology Stabilization (v1.0 Path)

- Formalize review workflow steps
- Clarify scoring definitions and scales
- Standardize output artifact structure
- Define required vs optional evaluation components

Goal: Achieve a stable, reproducible review methodology.

---

## 2. Scoring Normalization & Auditability

- Explicit scoring rubric documentation
- Calibration examples across multiple papers
- Inter-reviewer consistency guidance
- Audit trail template for evaluations

Goal: Improve reliability and defensibility of scores.

---

## 3. Automation & Tooling

- [Implemented] Structured input templates for review scaffolding (`dpi-lab scaffold`)
- [Implemented] Machine-readable review output schemas (metadata + scorecard)
- [Implemented] Script-assisted evaluation and validation workflow (`dpi-lab review`, `dpi-lab validate`)
- [Implemented] Governance support tooling for risk registers, evidence bundles, and scorecards under `tools/`
- [Implemented] Portable JSON review bundle export (`dpi-lab bundle`)
- [Planned] PDF-ready renders

Goal: Reduce manual friction and increase repeatability.

---

## 4. Comparative & Meta-Analysis Layer

- [Implemented] Framework for comparing multiple papers (`dpi-lab compare`)
- Thematic clustering model
- Governance gap index
- Cross-paper risk matrix synthesis
- [Implemented] Case-study structure for representative DPI-AI deployments under `case-studies/`

Goal: Elevate the lab from single-review outputs to ecosystem analysis.

---

## 5. Evidence & Citation Discipline

- [Implemented] Citation integrity guidance
- [Implemented] Source traceability via portable bundle export and manifest linking
- [Implemented] Explicit assumption logging scaffold
- [Implemented] Claim verification log scaffold

Goal: Increase epistemic rigor.

---

## 6. Conformance Declaration Model

- Template for declaring adherence to the Lab methodology
- Versioned methodology reference in outputs
- Change log for scoring criteria evolution
- [Implemented] Explicit Lab ↔ Artifacts compatibility contract for the v0.6.0 / v0.9.0 pairing

Goal: Treat the methodology itself as governable infrastructure.

---

## 7. Publication-Grade Output Refinement

- Standard executive summary template
- Structured risk register output
- Reusable visual tables
- Repository output consistency checks
- [Implemented] Reference governance architecture and maturity model guidance

Goal: Ensure professional-grade, publishable artifacts.

---

## 8. Ecosystem Threat Modeling

- [Implemented] DPI AI ecosystem threat model
- [Implemented] Agentic AI governance threat model
- Extend threat libraries with sector-specific overlays

Goal: Make systemic harm legible before it becomes a procurement requirement written in panic.

---

## Tracking Philosophy

This roadmap captures structural evolution, not delivery commitments.
Priorities may shift as research and ecosystem feedback evolve.

No schedule is implied.

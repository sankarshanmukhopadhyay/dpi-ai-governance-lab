# DPI AI Governance Lab — Evaluation Contract (Methodology v1.0)

## Status
**Normative.** This document defines the minimum required structure and evidence expectations for reviews produced in this repository.

## TRACE (what it stands for)
**TRACE (Trust, Risk, Architecture & Conformance Evaluation)** is the Lab’s named method for assessing DPI–AI systems, programs, and policies. TRACE is designed to produce **auditable outputs**, not aspirational principles.

See also: `docs/trace/README.md`

## Purpose
This contract ensures reviews are **repeatable, auditable, and comparable** across papers, reviewers, and time.

## Scope
Applies to:
- Paper reviews in `reviews/`
- Calibration examples in `calibration/`

Does not apply to:
- Exploratory notes not intended as “reviews”
- External summaries not scored under this methodology

## Definitions
- **Review Package**: The complete folder under `reviews/YYYY-MM-DD-<paper-slug>/`.
- **Rubric**: The scoring rules defined in `methodology/scoring-rubric.md`.
- **Audit Trail**: The evidence + rationale record defined by `templates/audit-trail-template.md`.

## Required outputs (MUST)
Each Review Package MUST contain the following files:

1. `README.md`
   - MUST provide quick navigation and include the paper link(s).

2. `01-summary.md`
   - MUST include: paper citation, 5–10 bullet summary, declared scope, and key claims.

3. `02-methodology-application.md`
   - MUST include: how the methodology was applied, assumptions, and boundaries.

4. `03-scorecard.md`
   - MUST include: completed rubric table + brief rationale per dimension.

5. `04-audit-trail.md`
   - MUST include: evidence references for each score, with traceability to paper sections.

6. `05-alignment-mapping.md`
   - MUST include: mapping to relevant governance artifacts and concepts (e.g., TRACE dimensions, operational packs, control families).

## Evidence & traceability (MUST)
For every scored dimension:
- The review MUST provide **at least one evidence pointer** (section, page, figure, table, or quote snippet ≤ 25 words).
- The audit trail MUST state whether the evidence is **explicit** (directly stated) or **inferred** (derived by interpretation), and SHOULD minimize inference.

## Required vs optional evaluation components

### Required components (MUST)
- Completion of the full scoring rubric (all dimensions)
- Score rationales that reference evidence
- Audit trail completion
- Stated scope, assumptions, and limitations
- Alignment mapping to governance artifacts

### Optional components (MAY)
- Comparative benchmarking against other papers
- Implementation feasibility analysis
- Policy recommendations or normative critique
- “Operator notes” for adoption teams

Optional components MUST NOT be used to compensate for missing required components.

## Scoring rules (MUST)
- Scores MUST use the defined scale in `methodology/scoring-scale.md`.
- If evidence is insufficient, the reviewer MUST score conservatively and explicitly mark the uncertainty.
- The reviewer MUST avoid “nice sounding” scoring. Only operational criteria qualify.

## Reproducibility standard (target)
A second reviewer, using the same rubric and evidence, SHOULD be able to reproduce scores within **±1 point per dimension**.
If not, the review MUST include a note explaining the ambiguity.

## Versioning & change control (MUST)
Each review MUST record:
- Methodology version
- Rubric version
- Any deviations (with rationale)

Changes to methodology/rubric MUST be logged in `meta/methodology-changelog.md`.

## Quality gate (definition of “complete review”)
A review is complete only when:
- All required outputs are present
- Rubric is fully scored
- Audit trail is complete and evidence-linked
- Alignment mapping is present

## Non-goals
This methodology does not attempt to:
- Determine “truth” of paper claims
- Provide legal compliance determinations
- Replace formal audit or certification

## Companion packs (Artifacts repo)
Reviews SHOULD include alignment mapping to the operational packs in the companion repository:

- `dpi-ai-governance-artifacts`

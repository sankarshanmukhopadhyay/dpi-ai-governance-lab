# Inter-reviewer Consistency Guidance (v1.0)

This guidance exists to keep scores **stable** across reviewers and over time.

## Core rules
- Prefer **evidence-linked** scoring over interpretive scoring.
- If evidence is ambiguous, score lower and record uncertainty.
- Treat “future work” as **not implemented** unless the paper provides an operational mechanism.

## Disagreement handling (SHOULD)
When reviewers differ by more than ±1 in any dimension:

1. Identify whether the disagreement is due to:
   - Different evidence interpretation
   - Different assumptions about scope
   - Different use of scoring anchors

2. Re-check scoring anchors in `methodology/scoring-scale.md`.

3. Record:
   - The evidence each reviewer relied on
   - The assumption(s) driving divergence
   - A reconciled score and rationale (or a documented split score)

## Rubric evolution (MUST)
If repeated disagreements occur on the same dimension:
- Propose an update to rubric language
- Log the change in `meta/methodology-changelog.md`
- Add a calibration example if needed

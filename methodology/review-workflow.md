# Review Workflow (Methodology v1.0)

This workflow is the **minimum stable path** for producing a complete, auditable review package.

## TRACE (what it stands for)
**TRACE (Trust, Risk, Architecture & Conformance Evaluation)** is the Lab’s named method for DPI–AI assessments. This workflow operationalizes TRACE for paper reviews.

## Steps (MUST)

1. **Intake & scope framing**
   - Capture the paper reference, link(s), and declared context.
   - Record what is explicitly in-scope vs out-of-scope for this review.

2. **First-pass extraction**
   - Extract key claims, system model elements, and risk/control assertions.
   - Record quotes/snippets (≤ 25 words) and page/section pointers for later evidence.

3. **Rubric pass (initial scoring)**
   - Score D1–D10 using `methodology/scoring-rubric.md`.
   - Write a 1–3 sentence rationale for each score.

4. **Evidence pass (audit trail)**
   - For each dimension, attach at least one evidence pointer (section/page/figure/table).
   - Mark evidence as **explicit** or **inferred**.

5. **Calibration check**
   - Compare scoring anchors against `calibration/` examples.
   - If your scores deviate materially, record the reason.

6. **Alignment mapping**
   - Map findings to Lab/Artifacts governance concepts: controls, operational packs, conformance surfaces.
   - Capture “what artifacts would be required to make this auditable in practice.”

7. **Package & publish**
   - Ensure all required files exist (contract compliance).
   - Update the review folder `README.md` with navigation and summary.

## Completion gate
A review is complete only if it passes the quality gate in `methodology/evaluation-contract.md`.

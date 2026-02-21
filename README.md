# DPI AI Governance Lab

The DPI AI Governance Lab is a structured, repeatable methodology for transforming AI and DPI policy papers into enforceable governance artifacts.

This repository is not a narrative archive. It is a **workbench**.
A paper review is treated as a build process: fixed inputs → fixed outputs → validators.

---

## Purpose

Most AI governance papers are directionally correct but operationally vague.
The Lab applies a deterministic review workflow to:

- Extract architectural primitives
- Surface institutional risk structures
- Bind risks to workflow tiers
- Define accountability and escalation models
- Translate insights into reusable governance artifacts

The goal is operational clarity, not commentary.

---

## Repository Structure

```
artifacts/     Reusable governance artifacts (control mappings, tier models, templates)
reviews/       Per-paper structured reviews
papers/        Source documents or paper packs
docs/          Methodology and reference documentation
data/          Control IDs, taxonomies, shared reference tables
schemas/       Machine-readable structures
tools/         Validators, generators, linters
```

### Conceptual Separation

- `artifacts/` = normative governance building blocks
- `reviews/` = instantiations of the methodology applied to specific papers
- `data/` and `schemas/` = shared validation and taxonomy backbone
- `tools/` = validation and reproducibility layer

---

## Quickstart

### 1) Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Run a deterministic review from a PDF

This creates a **structurally correct**, deterministic baseline review using the local engine (no external services).

```bash
dpi-lab review --pdf /path/to/paper.pdf --slug my-paper --out reviews/2026-xx-paper-batch
```

Outputs land in:

```
reviews/2026-xx-paper-batch/my-paper/
  paper.pdf
  extracted/
    paper.text.v1.txt
    paper.pdf.sha256
    paper.text.v1.sha256
  run/
    manifest.json
  paper-analysis.md
  paper-review-report.md
  paper-review-metadata.yaml
  paper-review-scorecard.yaml
```

### 3) Validate the output contract

```bash
dpi-lab validate reviews/2026-xx-paper-batch/my-paper
```

---

## How to Review Any Paper (Method)

Full method reference: `docs/methodology.md`

The Lab workflow:

1. Extract Architectural Primitives
2. Identify Institutional Risk Surfaces
3. Bind Risk to Workflow Tiers
4. Define Accountability + Escalation
5. Convert to Governance Artifacts

---

## Required Outputs (Contract)

Every review MUST produce:

- `paper-analysis.md`
- `paper-review-report.md`
- `paper-review-metadata.yaml`
- `paper-review-scorecard.yaml`

These files ensure cross-paper comparability and enable structured scoring.

Scorecards use integer scores on a **0..5** scale (inclusive).

---

## Tools

- CLI (recommended):
  - `dpi-lab extract|scaffold|review|validate|lint`
- Standalone scripts (also usable):
  - `tools/validators/validate_scorecard.py <scorecard.yaml>`
  - `tools/validators/validate_dossier.py <dossier.json>`
  - `tools/generators/new_review_scaffold.py --slug ... --out ...`
  - `tools/linters/lint_markdown.py <paths...>`

---

## Review Batches and Evolution

The repository may contain both:

- `reviews/2026/...` (legacy structure)
- `reviews/<date>-paper-batch/...` (current structure)

Future reviews should follow the batch-first structure for consistency.

---

## Design Philosophy

Governance must be operational.

Narratives persuade.
Artifacts enforce.

The DPI AI Governance Lab prioritizes enforceable structure over rhetorical positioning.

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

### 1) Install (pip)

```bash
python -m venv .venv
source .venv/bin/activate
pip install .
dpi-lab --version
```

> `pip install -r requirements.txt` is still supported for development, but releases are expected to be installable via `pip install .`.


### 2) Run a deterministic review from a PDF

This creates a **structurally correct**, deterministic baseline review using the local engine (no external services).

```bash
dpi-lab review --pdf /path/to/paper.pdf --slug my-paper --out reviews/2026-xx-paper-batch
```

### Optional: model-backed deterministic review (OpenAI)

This engine generates **schema-valid JSON** and then renders deterministic YAML/Markdown artifacts.
It also saves the **exact prompts** and **raw response payload** for audit and replay.

For long papers, the OpenAI engine automatically switches to **deterministic chunking + multi-pass summarization**
(map: per-chunk digests → reduce: final artifacts). This prevents truncation while keeping runs replayable.
You can tune limits via `--max-input-chars`, `--chunk-max-chars`, and `--chunk-max-count`.

For better control, the OpenAI engine also supports **token-aware budgets** (uses `tiktoken` when available):
`--max-input-tokens` and `--chunk-max-tokens`. If set, token budgets take precedence over character budgets.

If a schema-constrained call still fails (rare, but possible in the real world), the engine performs a **bounded repair retry**
and persists the raw payload for debugging.

```bash
export OPENAI_API_KEY="..."
dpi-lab review --engine openai --model gpt-5 \
  --pdf /path/to/paper.pdf --slug my-paper --out reviews/2026-xx-paper-batch
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

Validation levels:

```bash
# Contract-only (required files exist)
dpi-lab validate reviews/2026-xx-paper-batch/my-paper --level contract

# Contract + schema (default)
dpi-lab validate reviews/2026-xx-paper-batch/my-paper --level schema

# Contract + schema + light policy checks (recommended)
dpi-lab validate reviews/2026-xx-paper-batch/my-paper --level policy

# Optional semantic validation (engine-backed; requires API key for model engines)
dpi-lab validate reviews/2026-xx-paper-batch/my-paper --level semantic --engine openai --model gpt-5
```


### 4) Follow a guided walkthrough (recommended)

- Walkthrough: `docs/walkthrough.md`
- Example outputs: `reviews/examples-batch/` (offline, deterministic, onboarding-focused)

The walkthrough uses the example directories to explain the full lifecycle: extraction → scaffolding → generation → validation, plus how the manifest and hashes support audit and replay.

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

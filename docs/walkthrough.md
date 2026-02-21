# Workbench Walkthrough: From PDF to Deterministic Review Outputs

This walkthrough is a **hands-on tour** of the DPI–AI Governance Lab workbench. It shows what happens when you:

1) ingest a research paper (PDF)
2) extract and canonicalize text (deterministic)
3) generate a review directory (contracted outputs)
4) validate outputs against schemas and rules

The goal is not to “wow” with prose. The goal is to make the workflow **repeatable, inspectable, and auditable**.

> **Example-first**: The repository includes a set of example review directories under `reviews/examples-batch/`.
> These were generated with the **`local` engine** (offline deterministic stubs) so every user can reproduce the structure without API keys.

---

## 1. The Review Contract (what every run must produce)

A successful run produces four required artifacts in the review directory:

- `paper-analysis.md` — structured analysis notes aligned to Lab doctrine
- `paper-review-report.md` — readable report suitable for sharing
- `paper-review-metadata.yaml` — paper identifiers + run metadata (schema validated)
- `paper-review-scorecard.yaml` — rubric-aligned scores (schema validated)

Everything else is supporting evidence for determinism and auditability.

---

## 2. Open a real example directory

Pick one example directory (any will do). For instance:

`reviews/examples-batch/cdpi-dpi-ai-framework-2026/`

Inside you’ll see:

- `paper.pdf` — the input source
- `extracted/` — deterministic extraction outputs + hashes
- `run/` — run manifest + (for model engines) prompts and raw responses
- the **four required review artifacts**

This directory is the “unit of work” for the lab.

---

## 3. Deterministic extraction: why `extracted/` exists

The workbench treats PDF extraction like a build step. The key principle is:

> **If the extracted text isn’t stable, the review can’t be stable.**

In `extracted/` you will typically see:

- `paper.text.v1.txt` — canonicalized plain text
- `paper.pages.v1.json` — per-page canonical representation used for chunking
- `*.sha256` — hashes that pin the input and the canonical text to a specific run

These artifacts let you answer: *“Exactly what text did the engine see?”*

---

## 4. Run manifest: the reproducibility spine

Open:

`run/manifest.json`

This records:

- the **engine** used (`local`, and later `openai`, etc.)
- the key engine parameters (model name, temperature, seed if supported)
- the extraction hashes (PDF + canonical text)
- chunking settings (char/token budgets) when relevant
- the output files produced

Think of the manifest as the workbench’s “bill of materials.”

---

## 5. Generation workflow (extract → scaffold → generate → validate)

### 5.1 Install and run (offline deterministic)

From the repo root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python -m dpi_lab review --engine local \
  --pdf /path/to/paper.pdf \
  --slug my-paper \
  --out reviews/examples-batch

python -m dpi_lab validate reviews/examples-batch/my-paper
```

This produces the full directory contract and validates it locally.

### 5.2 Model-backed generation (contentful outputs)

Model-backed engines produce richer analysis/report content while still keeping the outputs schema-valid and auditable.

```bash
export OPENAI_API_KEY="..."

python -m dpi_lab review --engine openai --model gpt-5 \
  --pdf /path/to/paper.pdf \
  --slug my-paper \
  --out reviews/examples-batch

python -m dpi_lab validate reviews/examples-batch/my-paper
```

In model-backed runs, you’ll also see:

- `run/prompts/` — the exact prompts used (for replay)
- `run/responses/` — raw response payloads (for audit)

---

## 6. Validation: what is enforced (and why)

Validation is designed to be **engine-agnostic** by default.

When you run:

```bash
python -m dpi_lab validate <review-dir>
```

the validators check:

1) **Directory contract** — required files exist
2) **Schema validity** — YAML/JSON conforms to the schemas in `schemas/reviews/`
3) **Policy rules** — ranges, required keys, and other governance constraints

This ensures that reviews are structurally consistent and machine-checkable, regardless of which engine generated them.

---

## 7. How chunking works (for long PDFs)

Long papers can exceed model context limits. The workbench addresses this without truncation by using:

- deterministic per-page extraction (`paper.pages.v1.json`)
- deterministic chunking (contiguous page ranges)
- multi-pass generation (map → reduce) for model engines

Chunk IDs and hashes are stable, and chunking parameters are recorded in `run/manifest.json`.

---

## 8. Where the methodology shows up in outputs

The workbench intentionally separates:

- **doctrine** (what the lab cares about) — in `artifacts/`
- **method** (how to operationalize doctrine) — in `docs/` + templates
- **instances** (paper-specific work) — in `reviews/`

So when you read:

- `paper-review-report.md` — you’re seeing the “shareable” narrative
- `paper-analysis.md` — you’re seeing the traceable analysis aligned to the lab’s control surfaces
- `paper-review-scorecard.yaml` — you’re seeing the rubric projection into numeric structure

The scorecard is not “truth.” It is a **measurement interface**.

---

## 9. Suggested onboarding exercise

To internalize the workflow, do this once:

1) Pick any example directory under `reviews/examples-batch/`.
2) Inspect `extracted/` and `run/manifest.json`.
3) Run `validate` on it.
4) Re-run the same PDF under a model engine and compare:
   - schema still holds
   - prompts/responses are persisted
   - outputs are richer but remain contract-compliant

This is the intended “learning loop” for the workbench.

---

## 10. What “deterministic” means here (honest version)

- Extraction, scaffolding, rendering, schemas, and validation are designed to be **deterministic**.
- Model-backed generation is designed to be **auditable and replayable**.

Provider model updates can change outputs over time. The workbench mitigates this by persisting prompts, parameters, and hashes.

That’s the right trade: **high integrity over false certainty**.

# Tools

Helpers for validation, linting, and scaffolding.

This directory is intentionally small and dependency-light. The goal is
to make the repo verifiable on any machine with Python 3 installed.

## Validators

Validators are CLI scripts that return non-zero exit codes on failure.

- `tools/validators/validate_scorecard.py <scorecard.yaml>`
  - Validates the required score fields and basic value integrity.
  - Score range enforced: **0..5** (inclusive).
- `tools/validators/validate_dossier.py <dossier.json>`
  - Validates presence of required dossier fields.

## Generators

- `tools/generators/new_review_scaffold.py` creates a new review folder
  with the required contract files.
- `tools/generators/new_artifact_scaffold.py` scaffolds a new reusable
  artifact under `artifacts/`.

## Linters

- `tools/linters/lint_markdown.py` runs basic markdown hygiene checks.

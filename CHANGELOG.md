# Changelog

## [0.7.0] - 2026-03-16

### Summary

Infrastructure release. This version resolves CI build errors carried since v0.6.0, removes committed build artefacts, hardens housekeeping discipline, and adds GitHub Pages. No changes to the TRACE methodology, schemas, CLI behaviour, or governance artifacts.

### Fixed

- `CITATION.cff`: updated `version` field to `0.7.0` and `date-released` to `2026-03-16`.
- `.github/workflows/ci.yml`: removed broken reference to `reviews/examples-batch/cdpi-dpi-ai-framework-2026/paper.pdf` (PDFs are not committed to the repository). The offline smoke review step is replaced with `dpi-lab validate reviews/examples-batch`, which tests the same pre-built outputs without requiring a local PDF. A comment documents why full smoke review is local-only.
- Removed committed `build/` directory and `dpi_ai_governance_lab.egg-info/` from the repository tree. These are Python packaging artefacts that should not be tracked.
- Removed 16 `.DS_Store` files from `reviews/`, `reviews/examples-batch/`, `reviews/_examples/`, `reviews/2026/`, `papers/`, and the repository root.
- Removed all `__pycache__/` directories and `.pyc` files from the tracked tree.

### Added

- `.github/workflows/pages.yml`: GitHub Actions workflow deploying the repository to GitHub Pages on every push to `main`.
- `_config.yml`: Jekyll/primer theme configuration for GitHub Pages.
- `index.md`: curated landing page for the GitHub Pages site.
- `.github/workflows/ci.yml`: new hygiene gate step that fails CI if `.DS_Store`, `.pyc`, `__pycache__`, or `build/` are re-introduced.

### Changed

- `.gitignore`: hardened to cover `__pycache__/`, `*.pyc`, `*.pyo`, `build/`, `dist/`, `*.egg-info/`, `.pytest_cache/`, `.venv/`, editor files, and `/tmp/`.
- `docs/documentation-freshness.md`, `docs/overview.md`, `docs/INDEX.md`, `docs/contracts/lab-artifacts-interface.md`, `README.md`: updated `last_reviewed` dates to 2026-03-16 as part of scheduled Tier 0 freshness sweep.
- `TRACE_COMPATIBILITY.json`: added `{ "lab": "0.7.0", "artifacts": "1.0.0", "status": "supported" }` compatibility entry.
- `VERSION`: bumped to `0.7.0`.
- `pyproject.toml`: version bumped to `0.7.0`.

### Notes

- GitHub Pages requires manual activation in repository settings: Settings → Pages → Source → **GitHub Actions**.
- No changes to TRACE method version (`0.1.0`), review schemas, CLI commands, or governance artifacts in this release.

## Unreleased

## [0.6.0] - 2026-03-14

### Added
- DPI-specific threat models for ecosystem-scale public-sector deployments and agentic AI operating environments (`docs/threat-models/`).
- Reference governance architecture and public-interest case studies to connect TRACE analysis to deployable operating models (`docs/architecture/`, `case-studies/`).
- Governance maturity model and lightweight tooling for evidence bundles, risk registers, and scorecards (`maturity-model/`, `tools/`).

### Changed
- Updated the Lab ↔ Artifacts compatibility contract for the new release pair (`TRACE_COMPATIBILITY.json`).
- Refreshed README and documentation index so the repo reads less like a research shelf and more like an operator workbench.

### Fixed
- Removed OS cruft and synchronized version metadata across `VERSION`, `pyproject.toml`, and compatibility docs.


## [0.5.0] - 2026-03-05

### Added
- Repository release version file (`VERSION`) and version synchronization across docs.
- Deterministic Lab ↔ Artifacts contract stub (`docs/contracts/lab-artifacts-interface.md`) to make review outputs composable with operational packs.

### Changed
- CI now runs end-to-end: install, CLI smoke test, offline smoke review, and validation of bundled examples.
- Link checking now validates internal + external links using `lychee` (replacing placeholder job).

### Fixed
- Corrected malformed GitHub Actions workflow YAML that previously placed steps outside the job.
- Removed OS cruft (`.DS_Store`) and enforced ignore rules.

## [0.4.1] - 2026-02-21

### Added
- Engine-selectable semantic validation tier (`dpi-lab validate --level semantic --engine ...`).
- Semantic validation schema (`schemas/reviews/semantic-validation.schema.json`) and persisted results at `run/semantic-validation.json`.

### Changed
- `dpi-lab validate` now accepts a review directory *or* a directory tree and supports `--level` (contract/schema/policy/semantic).

## [0.4.0] - 2026-02-21

### Added
- Pip-installable workbench with `dpi-lab` CLI.
- Deterministic PDF extraction + hashing + manifests.
- Schema-based validation and offline smoke-test workflows.
- Examples batch and guided walkthrough for onboarding.

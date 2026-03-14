# Changelog

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

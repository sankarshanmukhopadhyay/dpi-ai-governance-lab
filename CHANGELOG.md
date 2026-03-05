# Changelog

## Unreleased

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

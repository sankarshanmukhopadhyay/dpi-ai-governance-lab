# Changelog

## Unreleased
- Restructured repo with artifacts + reviews + tools.

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
- Linked operational artifacts repository and clarified cross-repo alignment.

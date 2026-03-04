# Changelog

## Unreleased

### Added
- Agent governance artifacts and conformance profile updates aligned to agentic risk management (registration, mandates, containment, monitoring, shutdown).
- Reference bibliography updated to include Andrew Clearwater’s agent governance showdown (Mar 03, 2026).

### Fixed
- Removed stray `.DS_Store` from repository root.

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

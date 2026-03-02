# TRACE ↔ TSAM (Forward Reference)

This repository uses TRACE as its primary governance and risk analysis method for DPI AI systems.

For operationalization (assurance engineering), TRACE MAY be paired with TSAM (Trust Systems Assurance Method), which defines how governance intent is bound to:

- Assurance levels
- Conformance verification
- Runtime integrity controls
- Evidence & observability

Canonical relationship document (source of truth):

- TRQP Assurance Hub: `docs/strategy/TRACE-TSAM-relationship.md`

Local companion artifacts:

- TRACE→TSAM compliance matrix (YAML): `docs/trace/trace-tsam-compliance-matrix.yaml`
- DPI AI annex templates:
  - `docs/annexes/dpi-ai-trace-tsam-annex.md`
  - `docs/annexes/dpi-ai-trace-tsam-annex.yaml`

This repo MUST NOT maintain a divergent normative copy of the canonical relationship document. Changes SHOULD be made in the canonical source and propagated as synchronized mirrors where required.

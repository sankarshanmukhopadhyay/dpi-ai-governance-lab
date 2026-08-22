# Changelog

## [Unreleased]

## [0.9.0] - 2026-08-22

### Summary

Implementation-readiness and harms release. This version makes the Lab substantially easier to adopt from a system-building starting point and stabilizes an operational AI-harm analysis contract through non-corpus pressure testing.

### Added

- Implementation-first onboarding path from system proposition to governance gap, capability, remediation, negative tests, evidence and TRACE verification.
- Task-oriented Start Here guidance for teams that want to build rather than begin with publication review.
- Minimum viable evidence and implementation-readiness definitions for governed systems.
- Machine-readable `schemas/harms/harm-chain.schema.json` for causal, evidence-bearing harm analysis.
- Reusable harm-chain template, worked example and CI validator.
- Twelve-class operational DPI/AI harm taxonomy covering exclusion, differential error, automation bias, data/provenance harm, privacy/correlation, authority abuse, accountability diffusion, drift, manipulation/synthetic evidence, security/supply-chain harm, correction/remedy failure, and population-scale compounding harm.
- Harm-oriented adversarial checklist separating model risk, governance failure, experienced harm, propagation, redress, residual risk and closure evidence.
- Non-Digital-Statecraft stabilization fixtures for welfare fraud detection and a delegated entitlement agent.
- Reader-facing executable entitlement-agent guide documenting authority, runtime enforcement, negative paths and minimum evidence.

### Changed

- README and Pages navigation now treat evaluation-first and implementation-first use as equal entry paths.
- Digital Statecraft is positioned as proof of method rather than a corpus-expansion requirement.
- Harm analysis now separates preventive, detective and corrective controls and binds redress/remedy to closure evidence.
- Harm-chain validation covers the canonical example plus two materially different non-corpus pressure fixtures.
- Lab ↔ Artifacts compatibility contract now records Lab `0.9.0` with Artifacts `1.1.0` as supported.

### Stabilization evidence

The operational harm-chain model was exercised against:

- welfare fraud detection — false-positive model signal, automation bias, wrongful benefit suspension and delayed remedy;
- delegated entitlement agent — scope, revocation, runtime authorization, effect correlation and redress failure.

Both cases validated without a structural change to the harm schema. The exercise exposed a documentation gap, not a schema gap: the executable entitlement-agent case lacked reader-facing implementation guidance, which is now supplied.

No new Artifacts capability was justified by the pressure tests; existing bounded-delegation, inference-traceability, evidence-closure, redress and correction-propagation capabilities were sufficient for the selected cases.

### Notes

- TRACE method version remains `0.1.0`.
- The harm taxonomy is jurisdiction-neutral and does not itself establish legal conclusions or risk acceptance.
- Candidate capability mappings are pressure-test outputs, not claims that every harm is solved by an existing artifact.
- Reference-case success is not production certification.

## [0.8.0] - 2026-08-22

### Summary

Substantive operator-workbench release. This version demonstrates the complete TRACE governance-improvement loop against a frozen public Digital Statecraft DPI corpus: source selection, reproducible evaluation, normalized governance gaps, cross-repository remediation demand, adversarial implementation, evidence-backed synthetic closure, and re-evaluation.

### Added

- Governance-gap contract and validation for `GAP-*` → `CAP-*` remediation handoff.
- Executable-governance preview and bounded-delegation closure fixtures.
- Frozen six-post Digital Statecraft DPI corpus with deterministic provenance validation.
- Six reproducible TRACE review bundles and 19 evidence-backed implementation-distance gaps.
- Corpus-level recurring-gap and remediation baseline with immutable historical coverage metrics.
- Worked public-benefit eligibility/payment fixture exercising all six recurring capability classes across positive and adversarial paths.
- Machine-readable programme summary and CI validator for headline before/after/closure metrics.
- Operator-first Just-the-Docs information architecture, Pages manifests, front-matter validation, diagrams, and end-to-end worked demonstration.
- Portable review bundle export, comparative matrix generation, optional assumption logs, and claim-verification logs.

### Changed

- TRACE operator workflow now explicitly supports `Evaluate → Find → Normalize → Remediate → Implement → Verify → Re-evaluate`.
- Lab ↔ Artifacts compatibility contract now records the `0.8.0` / `1.1.0` supported release pair.
- Documentation distinguishes historical remediation coverage, current remediation mapping, synthetic fixture closure, and publication-level closure as separate assurance claims.

### Evidence milestone

Digital Statecraft first-wave programme:

- 6 publications / 6 TRACE reviews
- 19 material gaps across 6 recurring capability classes
- historical Artifacts registry 0.2.0: 10/19 standardized mappings (52.63%)
- current Artifacts registry 0.5.0: 19/19 mappings (100%)
- worked fixture: 6/6 selected capabilities pass scoped closure criteria across 9 scenarios, including 8 adversarial paths
- publication-level closures: 0 by design

### Notes

- Synthetic closure is scoped to the declared fixture and is not certification of a production deployment.
- Publication-level findings are not closed merely because reusable remediation exists.
- TRACE method version remains `0.1.0`.

## [0.7.0] - 2026-03-16

### Summary

Infrastructure release. This version resolves CI build errors carried since v0.6.0, removes committed build artefacts, hardens housekeeping discipline, and adds GitHub Pages. No changes to the TRACE methodology, schemas, CLI behaviour, or governance artifacts.

### Fixed

- `CITATION.cff`: updated `version` field to `0.7.0` and `date-released` to `2026-03-16`.
- `.github/workflows/ci.yml`: removed broken reference to `reviews/examples-batch/cdpi-dpi-ai-framework-2026/paper.pdf`.
- Removed committed `build/`, egg-info, `.DS_Store`, `__pycache__`, and `.pyc` artefacts.

### Added

- GitHub Pages deployment workflow and site configuration.
- Curated Pages landing page.
- CI hygiene gates preventing common generated/OS artefacts from returning.

### Changed

- Hardened `.gitignore` and refreshed documentation freshness metadata.
- Added the `0.7.0` / `1.0.0` compatibility pair.

## [0.6.0] - 2026-03-14

### Added

- DPI-specific threat models for ecosystem-scale public-sector deployments and agentic AI operating environments.
- Reference governance architecture and public-interest case studies.
- Governance maturity model and lightweight tooling for evidence bundles, risk registers, and scorecards.

### Changed

- Updated Lab ↔ Artifacts compatibility contract.
- Refreshed README and documentation index toward an operator workbench.

### Fixed

- Removed OS cruft and synchronized version metadata.

## [0.5.0] - 2026-03-05

### Added

- Repository release version file and version synchronization.
- Deterministic Lab ↔ Artifacts contract stub.

### Changed

- CI runs install, CLI smoke test, offline smoke review, and validation of bundled examples.
- Link checking validates internal and external links.

### Fixed

- Corrected malformed GitHub Actions workflow YAML.
- Removed OS cruft and enforced ignore rules.

## [0.4.1] - 2026-02-21

### Added

- Engine-selectable semantic validation tier.
- Semantic validation schema and persisted results.

### Changed

- `dpi-lab validate` accepts a review directory or directory tree and supports contract/schema/policy/semantic levels.

## [0.4.0] - 2026-02-21

### Added

- Pip-installable workbench with `dpi-lab` CLI.
- Deterministic PDF extraction, hashing, and manifests.
- Schema-based validation and offline smoke-test workflows.
- Examples batch and guided walkthrough.

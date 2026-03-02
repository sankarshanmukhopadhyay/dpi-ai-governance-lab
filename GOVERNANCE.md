# Governance

This repository is maintained as an **implementation workbench** for the DPI AI Governance toolchain.

## Maintainers

- Maintainers are listed in `CODEOWNERS` (or the GitHub repository settings, for forks).

## Decision model

We default to a lightweight, explicit decision process:

- **Small changes** (docs, examples, non-breaking fixes): maintainer approval via PR review.
- **Schema / contract changes** (anything that changes validation outcomes or required artifacts):
  - MUST include a version bump (SemVer) and updated examples
  - MUST include tests (or test vectors) that demonstrate the change
  - SHOULD include a migration note in `CHANGELOG.md`
- **Methodology changes** (TRACE workflow semantics, scoring meanings, review pipeline):
  - MUST include an ADR-style note in `docs/decisions/` (short is fine)
  - SHOULD include cross-repo alignment update (see `TRACE_COMPATIBILITY.json`)

## Dispute handling

If there is disagreement:
1. Document the competing options in the PR description.
2. Maintainers make a decision and record the rationale (PR summary or ADR).
3. If still blocked, use a time-boxed discussion (7 days), then decide and move on.

## Release discipline

- Maintain `CHANGELOG.md` in a "write it when you merge it" posture.
- Releases are cut from the default branch and tagged.

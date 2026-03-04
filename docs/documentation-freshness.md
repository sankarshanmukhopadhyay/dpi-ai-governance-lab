---
last_reviewed: 2026-03-04
applies_to: main
owners:
  tier0: repo-maintainers
  tier1: repo-maintainers
  tier2: repo-maintainers
  tier3: repo-maintainers
---

# Documentation Freshness & Relevance

This repository treats documentation as a build artifact. The goal is simple: a reader should be able to start, navigate, and validate the methodology without guessing.

## Tiers and review SLAs

| Tier | Scope | Max age | Primary entrypoints |
|---|---|---:|---|
| Tier 0 | Onboarding and orientation | 30 days | `README.md`, `docs/overview.md` |
| Tier 1 | Method + interfaces (schemas, templates, CLI/API) | 60 days | `docs/`, `schemas/`, `templates/` (as applicable) |
| Tier 2 | Operational runbooks | 90 days | `.github/`, `docs/runbooks/` (as applicable) |
| Tier 3 | Architecture rationale (ADRs) | 180 days | `docs/adr/` (as applicable) |

## Freshness signals enforced in this repo

- Tier 0 docs declare `last_reviewed` and the branch they apply to.
- Internal links in Markdown are validated in CI.
- placeholder markers are not permitted in Tier 0 docs.

## How to run the docs audit locally

```bash
python scripts/docs_audit.py
```

## What changed in this review (2026-03-04)

- Removed OS metadata artifacts (e.g., `.DS_Store`) from the repository root.
- Resolved placeholder references in the UNESCO AI maturity framework example by linking to the canonical publication record.
- Added a repeatable internal Markdown link audit and freshness guardrails.

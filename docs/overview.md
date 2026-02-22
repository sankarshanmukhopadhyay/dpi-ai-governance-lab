# DPI AI Governance Lab

The **DPI AI Governance Lab** is a repo of **governance artifacts** used to review (and pressure-test) AI + DPI proposals, papers, and deployment plans.

## What this repo optimizes for

- Turning narrative claims into **deployable controls**
- Making governance **tier-aware** (not everything needs the same rigor)
- Making systems **auditable at runtime** (not just compliant on paper)
- Ensuring **redress and remedy** are first-class, testable requirements

## Core flows

1. **Review a paper** using `/reviews/templates/paper-review-report-template.md`
2. Classify the use-case via `/artifacts/risk-tiering/`
3. Require an **AI Deployment Dossier** for Tier 2–3 via `/artifacts/deployment-dossier/`
4. Bind controls via `/artifacts/conformance-profiles/`
5. Validate dossier/scorecards via `/tools/` + CI

## Legacy content

Earlier work remains available under `/papers`, `/templates`, `/schemas`, and `/profiles`.
New work should prefer `/artifacts` + `/reviews`.


## Operational artifacts

This methodology has a sister repository of operational packs and reusable governance building blocks:
- https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-artifacts

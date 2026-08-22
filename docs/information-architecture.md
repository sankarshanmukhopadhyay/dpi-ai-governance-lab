---
layout: default
title: Documentation architecture
nav_order: 6
---

# Documentation architecture

The rendered documentation is organized around user tasks rather than repository folders.

## Primary navigation

1. **Start here** — choose a task and understand the improvement loop.
2. **Operator playbook** — move from gap to implementation and closure.
3. **Evaluations** — inspect real reviews, gap baselines, recurring patterns, and re-evaluation.
4. **Method and evidence** — TRACE evaluation method, scoring, evidence discipline, and comparison.
5. **Verification** — executable governance, threat models, and assurance mechanisms.
6. **Reference** — schemas, contracts, maturity material, ADRs, and implementation detail.

## Repository versus site

The repository remains optimized for reproducibility and machine-verifiable artifacts. The Pages site is a curated reading layer over that repository. Not every repository file needs to appear in primary navigation; deep technical artifacts remain searchable and linkable.

## Cross-repository journey

The Lab site links operators to the companion Artifacts site at the point where a normalized capability needs remediation. The Artifacts site links back to the Lab for source findings and closure re-evaluation.

This separation preserves clear authority and responsibility while presenting one coherent operator workflow.

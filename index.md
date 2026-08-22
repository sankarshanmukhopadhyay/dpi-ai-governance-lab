---
layout: default
title: DPI AI Governance Lab
nav_order: 0
---

# DPI AI Governance Lab

**Evaluate → find gaps → remediate → verify improvement.**

The Lab is a TRACE workbench for people who design, procure, implement, operate, and assure DPI/AI systems. It turns publications and deployment propositions into evidence-backed findings, normalized governance gaps, remediation requirements, and closure tests.

{: .note }
The Lab is deliberately paired with the companion **DPI–AI Governance Artifacts** repository. The Lab identifies and normalizes the problem; the Artifacts repository supplies reusable implementation assets and evidence requirements.

## Choose your path

### Evaluate a publication

Start with [Start here](docs/start-here.md), then use the TRACE methodology, review workflow, and `dpi-lab` CLI to create a reproducible evaluation.

### Improve a deployment

Use the [Operator playbook](docs/operator-playbook.md) to move from a material gap to a capability, remediation asset, implementation change, test, and evidence-backed closure.

### See what repeated evaluations are teaching us

Go to [Evaluations](docs/evaluations.md). The [first real-review governance gap baseline](baselines/2026-08-22/README.md) re-expresses three existing substantive reviews as nine machine-readable gaps and identifies three recurring capability clusters.

### Build or test executable governance

Use [Executable governance](docs/executable-governance.md) as the verification layer once authority, remediation requirements, and closure evidence have been made explicit.

## Current programme signal

The first real-review baseline found the same three capability gaps across all three reviewed publications:

| Capability | Recurrence | Current remediation coverage |
| --- | ---: | --- |
| Bounded authority and delegation | 3/3 | Partial |
| Operational appeal and remedy | 3/3 | Standardized |
| Evidence-backed governance closure | 3/3 | Standardized |

This gives the programme an evidence-derived priority: strengthen authority/delegation remediation, then instantiate and test the standardized redress and evidence assets in a realistic deployment.

## Core tools

```bash
dpi-lab review --pdf paper.pdf --slug example --out reviews/batch
dpi-lab validate reviews/batch/example
dpi-lab gaps-validate reviews/batch/example/governance-gaps.yaml --summary
dpi-lab governance-validate case-studies/executable-governance-entitlement-agent
```

## Documentation architecture

- [Start here](docs/start-here.md) — task routing and concepts
- [Operator playbook](docs/operator-playbook.md) — implementation lifecycle
- [Evaluations](docs/evaluations.md) — reviews, baselines, recurring gaps, re-evaluation
- [TRACE Operator Improvement Loop](docs/operator-improvement-loop.md) — mission and cross-repo contract
- [Methodology](methodology/README.md) — evaluation method and scoring
- [Evidence discipline](docs/evidence-and-citation-discipline.md) — provenance and auditability
- [Executable governance](docs/executable-governance.md) — runtime verification preview

{: .warning }
TRACE findings, mappings, and closure assessments do not acquire jurisdictional, institutional, legal, procurement, or deployment authority. Those authorities remain with the responsible external actors.

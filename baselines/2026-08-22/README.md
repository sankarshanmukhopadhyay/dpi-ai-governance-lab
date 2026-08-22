---
layout: default
title: First real-review gap baseline
parent: Evaluations
nav_order: 2
---

# First real-review governance gap baseline

This baseline re-expresses three existing TRACE reviews through the governance-gap contract introduced in August 2026. It is a **rebaseline of existing review evidence**, not a fresh review of the source publications.

## Included reviews

1. **Vision Paper: DPI-AI Framework 2026 (CDPI)**
2. **Preparing India for AI Adoption: Challenges and Solutions**
3. **UNESCO AI Maturity Framework: A self-positioning guide for public administrations**

## Results

| Measure | Result |
| --- | ---: |
| Publications rebaselined | 3 |
| Material governance gaps encoded | 9 |
| Recurring capability clusters | 3 |
| Standardized remediation mappings | 6 |
| Partial remediation mappings | 3 |
| Gaps with no artifact mapping | 0 |
| Evidence-backed closed gaps | 0 |
| Artifact coverage | 100% |
| Standardized remediation coverage | 66.7% |
| Closure rate | 0% |

The 100% artifact coverage figure means every encoded gap currently has at least a partial mapping into the companion Artifacts repository. It **does not** mean the gaps are solved. The authority/delegation capability remains partial, and none of these publication-level gaps has implementation evidence sufficient for closure.

## Repeated gap clusters

### CAP-AUTHORITY-BOUNDED-DELEGATION — 3/3 reviews

All three reviews identify a missing or incomplete runtime authority model for consequential AI use: accountable decision rights, bounded delegation, tier gates, escalation, suspension/revocation, or rollback.

**Current remediation coverage:** partial.

This is therefore the highest-priority artifact-development signal from the first baseline.

### CAP-REDRESS-APPEAL — 3/3 reviews

All three reviews identify redress as present in principle but incomplete operationally: missing accountable ownership, appeal states, service levels, or remedy outcomes.

**Current remediation coverage:** standardized.

The next step is implementation evidence, not another template.

### CAP-EVIDENCE-CLOSURE — 3/3 reviews

All three reviews identify weak evidence hooks: missing audit artifacts, logs, test outputs, deployment dossiers, provenance, or explicit evidence-to-claim binding.

**Current remediation coverage:** standardized.

The next step is to instantiate evidence bundles against a realistic deployment and verify closure.

## Operator interpretation

This baseline changes the backlog from a catalogue-development problem into an evidence-derived implementation programme:

1. strengthen bounded authority/delegation artifacts because the gap recurs across all three reviews and coverage is partial;
2. instantiate the standardized redress and evidence remediation assets in a realistic deployment fixture;
3. run deterministic closure tests;
4. re-evaluate the fixture and record the before/after delta.

## Source gap registers

- `reviews/2026-02-20-paper-batch/dpi-ai-framework-2026/governance-gaps.yaml`
- `reviews/2026-02-20-paper-batch/preparing-india-for-ai-adoption/governance-gaps.yaml`
- `reviews/2026-02-20-paper-batch/unesco-ai-maturity-framework/governance-gaps.yaml`

## Authority boundary

The baseline owns the TRACE evaluation and remediation mapping only. It does not convert the reviewed publications, the Lab, or the companion artifact library into jurisdictional or deployment authorities.

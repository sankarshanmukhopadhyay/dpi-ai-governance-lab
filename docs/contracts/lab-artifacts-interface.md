# Lab ↔ Artifacts Interface Contract (v1)

Last reviewed: 2026-03-16

## Purpose

This contract defines the *stable interface* between:

- **dpi-ai-governance-lab** (the workbench): produces deterministic review outputs
- **dpi-ai-governance-artifacts** (the product surface): operational packs, controlled docs, schemas, templates

The goal is to make review outputs **composable** with operational packs without requiring hand-curation.

## What the Lab Produces (canonical review directory)

A Lab review directory **MUST** contain:

- `paper/` extracted text + metadata
- `run/` deterministic manifests and hashes
- `results/` structured findings and scores
- `evidence/` optional evidence bundles provided by reviewers

The Lab **SHOULD** persist machine-readable outputs as JSON/YAML alongside human-readable Markdown.

## How Artifacts Consume Outputs (pack alignment)

Artifacts packs **MAY** reference Lab outputs in two ways:

1. **Direct inclusion** (evidence bundle includes review outputs)
2. **Derived evidence** (review outputs drive which pack templates and controlled docs are required)

Pack selectors **SHOULD** be driven by:

- domain (public sector, redress, procurement, agent governance)
- risk profile (TRACE factors, scoring tiers)
- assurance expectations (evidence bundle depth)

## Versioning and compatibility

- `TRACE_VERSION` defines the method vocabulary.
- Repo `VERSION` defines packaging and automation semantics.

Compatibility is tracked in `TRACE_COMPATIBILITY.json` and must remain consistent across both repos.

## Non-goals

- This contract does not publish a threat model.
- This contract does not mandate external compliance claims.

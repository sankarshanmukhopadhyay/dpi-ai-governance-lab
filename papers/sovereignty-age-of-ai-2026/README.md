# Sovereignty in the Age of AI (TBI, Jan 2026) — Lab Extension Pack

This folder operationalizes the paper **“Sovereignty in the Age of AI: Strategic Choices, Structural Dependencies and the Long Game Ahead” (Jan 2026)** into governance artifacts that can be adopted inside DPI-aligned AI programs.

The source paper introduces:
- A layered **AI stack** lens (compute, energy, data, models, applications, talent/skills, governance)
- A posture taxonomy: **Control / Steer / Depend (CSD)**
- Strategy levers (interop, diffusion, access agreements, etc.)

The Lab extension pack converts this narrative into **proof-carrying governance**:
- measurable posture declarations,
- conformance expectations,
- runtime audit/trace requirements,
- resilience stress tests,
- a maturity model for sequencing.

## Contents

### 1) Posture → Proof
- `sovereignty-assurance-model.md` — control artifacts + runtime proofs per layer  
- `../schemas/sovereignty-age-of-ai-2026/posture-declaration.schema.json` — machine-readable posture declaration schema  
- `../schemas/sovereignty-age-of-ai-2026/posture-declaration.example.json` — example declaration

### 2) Quantification
- `sovereignty-readiness-index.md` — DPI-linked Sovereign AI Readiness Index (SARI)  
- `../schemas/sovereignty-age-of-ai-2026/sari-assessment.schema.json` — machine-readable SARI schema  
- `../schemas/sovereignty-age-of-ai-2026/sari-assessment.example.yaml` — example assessment

### 3) DPI as the Sovereignty Control Plane
- `dpi-ai-sovereignty-architecture.md` — reference architecture + minimum viable integration checklist

### 4) Interoperability = Exit Leverage
- `interoperability-exit-leverage-protocol.md` — Exit Leverage Protocol (ELP) and procurement clauses  
- `../templates/interoperability-conformance-checklist.md` — conformance checklist template

### 5) Runtime Governance
- `runtime-governance-framework.md` — policy-to-runtime mapping, logging, redress triggers, continuous eval

### 6) Energy–Compute Coupling Resilience
- `ai-infrastructure-resilience-playbook.md` — stress tests, drills, evidence expectations

### 7) Sequencing (Emerging Economy Pathway)
- `sovereignty-maturity-model.md` — Phase model: Access → Adapt → Embed → Influence

## How to use

1. Create a `posture-declaration.json` using the schema in `schemas/…/posture-declaration.schema.json`.
2. Run a SARI baseline using `templates/sari-assessment-template.yaml` (or the schema).
3. Translate gaps into a backlog using control IDs in `sovereignty-assurance-model.md`.
4. Bake interoperability + runtime governance clauses into procurement templates.
5. Institutionalize resilience drills using the playbook.

_Last updated: 2026-02-20_

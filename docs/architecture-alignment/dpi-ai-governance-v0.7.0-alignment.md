# DPI AI Governance v0.7.0 — Governance Lab Alignment Memo

## What changed in the Artifacts repository

DPI AI Governance Artifacts v0.7.0 introduces a structural shift:
- A governance spine (`governance/`) that defines scope, normativity, and revision discipline
- A controlled-document taxonomy (`controlled/`) organizing materials by governance function (risk, assurance, redress, etc.)
- Clear separation of policy vs rule vs schema vs profile vs evidence

The Artifacts repository is **compatible with** Trust Over IP (ToIP) structural discipline, but is **not** a ToIP-compliant Governance Framework.

---

## What this means for the Governance Lab

The Governance Lab remains methodologically independent (TRACE and review workflow do not change).

However, Lab outputs SHOULD align structurally by mapping findings and outputs to the Artifacts controlled-document taxonomy:

- **Risk** findings and register outputs → `controlled/risk/`
- **Assurance / conformance** findings and evidence expectations → `controlled/assurance/`
- **Redress / remediation** findings → `controlled/redress/`

This improves interoperability and reduces ambiguity for adopters consuming Lab reviews alongside the Artifacts repo.

---

## Practical guidance for Lab reviewers

When writing a review package:

1. Tag sections as **Risk**, **Assurance**, **Redress** explicitly.
2. When linking to reference artifacts, prefer new paths under `controlled/**`.
3. If you must refer to legacy paths from older releases, include a note: “migrated in v0.7.0 to `controlled/...`”.

---

## What does NOT change

- TRACE methodology and the Lab’s analytical approach
- Argument maps, executive summaries, and risk registers as outputs
- The Lab’s role as an evaluation engine (not a governance framework)

---

## Optional future integration (nice-to-have)

The Lab MAY later add automation that:
- Emits evidence bundles compatible with `controlled/assurance/evidence-bundles.md`
- Normalizes risk records into the Artifacts repo risk schema formats
- Generates remediation closure tracking aligned with redress expectations

None of these are required for current operation.

---

## Layering principle

- **Artifacts repo** defines governance architecture.
- **Governance Lab** evaluates systems and papers against that architecture.

Keeping this separation is a feature, not a limitation.

# Alignment mapping

This review is meant to be legible to adopters using the **DPI AI Governance Artifacts** operational packs.

## Key gap-closure targets (from migrated review notes)

- Add an explicit **risk-tiering model** that translates “assured” into enforceable requirements.
- Define an **assurance toolchain reference architecture** (what artifacts exist, who produces them, and how they are validated).
- Specify **ownership, metrics, and milestones** for delivery (accountability plumbing).

## Suggested artifact mappings (Artifacts repo)

- **Risk tiering:** `artifacts/risk-tiering/` (tier model + decision tree + scoring rubric)
- **Deployment dossier / evidence:** `artifacts/deployment-dossier/`
- **Runtime accountability:** `artifacts/runtime-accountability/` (incident escalation, RACI, rollback)
- **Evaluation & assurance:** `artifacts/evaluation-and-assurance/` (benchmark minimums, drift monitoring)

## TRACE mapping (Lab method)

- **Trust:** operational accountability + evidence expectations (D6–D8)
- **Risk:** structured harm model + tier binding (D3, plus tiering artifacts)
- **Architecture:** system and stakeholder model (D2)
- **Conformance:** testable controls + evidence bundles (D4, D8, D10)

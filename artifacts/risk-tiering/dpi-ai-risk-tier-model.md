# DPI AI Risk Tier Model (v0.1)

## Tiers

| Tier | Name | Typical behavior |
|---|---|---|
| 0 | Informational | Produces information only; no operational consequence |
| 1 | Operational support | Assists staff workflows; human decides |
| 2 | Rights-affecting decision support | Influences eligibility/entitlements/enforcement; contestable record required |
| 3 | Automated rights-affecting action | System triggers/executes consequential action; prohibited-by-default unless strict conditions met |

## Core scoring dimensions

- **Impact severity** (harm / rights / safety)
- **Scale** (population × frequency)
- **Reversibility** (rollback/remedy feasibility)
- **Opacity** (explainability + auditability)
- **Adversarial pressure** (incentives to game/attack)

## Default rule

If a system can **change outcomes** for a person, it is **not Tier 0**.
If a system can **deny/approve/trigger** without a human, it is **Tier 3**.

# ADR — TRACE Identity Legitimacy Positioning

## Status
Accepted

## Decision

TRACE **SHALL NOT** introduce Identity Legitimacy as an independent fifth axis.

TRACE **SHALL** include Identity Legitimacy as a **mandatory evaluation checkpoint** within its **Risk** and **Accountability/Trust** considerations.

TRACE **SHALL** require that any acting AI agent meet a recognized external identity assurance baseline (e.g., **Agent Name Assurance Baseline (ANAB) ALx** or equivalent).

TRACE **SHALL NOT** duplicate identity assurance threat models, annexes, or conformance ladders.

Identity assurance mechanics remain **external and composable**.

## Rationale

1. Identity legitimacy is foundational to agent governance and prevents misbinding/impersonation failure modes.
2. Duplication of identity assurance logic creates architectural coupling and long-term drift.
3. TRACE must remain composable, layered, and adoptable across contexts.
4. Governance of action and governance of identity are distinct but interdependent domains.
5. Long-term maintainability favors interface contracts over annex migration.

## Consequences

- DPI AI repos reference ANAB via a defined interface contract.
- TRACE documentation includes explicit Identity Legitimacy checkpoints.
- No identity annexes are migrated into DPI AI repos.
- A risk-tier ↔ assurance crosswalk is maintained (machine-readable where possible).

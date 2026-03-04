# Agent containment + kill-switch runbook (template)

Purpose: ensure rapid shutdown and harm containment for an operational agent.

## Preconditions
- Agent registry entry exists and is current.
- Operator on-call and escalation contacts are defined.
- Suspension and revocation mechanisms are tested.

## Actions
1. **Suspend** the agent (stop execution + tool calls).
2. **Revoke** credentials/tokens used by the agent.
3. **Freeze side-effects** (payments, writes, approvals) if applicable.
4. **Quarantine** runtime environment (network egress off, secrets rotated).
5. **Capture evidence** (action logs, delegation chain records, decision receipts).
6. **Initiate incident workflow** (root cause + remediation + redress triggers).

## Success criteria
- No new actions observed after suspend within defined window.
- All tool credentials revoked.
- Evidence bundle captured and stored.

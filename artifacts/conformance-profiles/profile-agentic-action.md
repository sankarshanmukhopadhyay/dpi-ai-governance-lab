# Conformance profile — Agentic action (starter)

This profile adds **agent-specific** governance expectations to the base profiles.

## Applicability
Use when a system can:
- invoke tools autonomously (especially with write-side effects),
- spawn or orchestrate multiple agents,
- maintain memory across sessions,
- operate continuously with minimal human oversight.

## Control expectations (minimum)

### AGT-01 Agent registry
- All operational agents MUST be registered, owned, and revocable.

### AGT-02 Mandates + authority boundaries
- Agents MUST operate under explicit mandates with scope, constraints, and expiry.
- Actions outside scope MUST be blocked or escalated.

### AGT-03 Delegation provenance
- Delegation chains MUST be reconstructable end-to-end for consequential actions.

### AGT-04 Containment + stop-rights
- Systems MUST implement tested kill-switch/suspension mechanisms.
- Stop-rights MUST be defined and binding.

### AGT-05 Continuous monitoring
- Post-deployment telemetry MUST detect runaway loops, anomalous tool use, and policy violations.

## Evidence requirements (minimum)
- Agent registry export + change history
- Signed mandates / delegation artifacts
- Sampled delegation chain logs linked to action logs
- Kill-switch drill logs
- Monitoring configuration + incident examples (sanitized)

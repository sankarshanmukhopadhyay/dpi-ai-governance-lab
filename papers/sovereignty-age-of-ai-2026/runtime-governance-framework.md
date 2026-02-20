# Runtime AI Governance Framework (RAGF)
## Policy-to-runtime enforcement for DPI-aligned AI systems

**Gap addressed.** The source paper discusses governance as an institutional trade-off (innovation vs assurance). This framework specifies **how governance executes at runtime**.

> If governance cannot constrain behavior at runtime, it is guidance, not governance.

---

## RAGF building blocks

### 1) Policy engine
- Encodes allowed scopes, prohibited actions, risk-tier constraints, and escalation triggers.
- Enforces: *who can do what, with which model, on which data, for which purpose.*

### 2) Trace and audit service
- Emits trace events for decision points and actions.
- Captures: inputs, provenance pointers, model/version, policy/version, outputs, and downstream effects.

### 3) Continuous evaluation
- Scheduled and event-driven evaluation pipelines:
  - drift detection
  - bias/regression checks
  - safety and misuse probes
  - domain performance

### 4) Redress + rollback
- Citizen-facing appeal paths for high-impact decisions.
- Operational rollback paths:
  - model rollback
  - policy rollback
  - workflow reversal (where feasible)
- Evidence retention with privacy protections.

### 5) Incident response
- Incident taxonomy (severity, scope, reversibility)
- Reporting SLAs and escalation matrix
- Post-incident review requirements (RCA + remediation evidence)

---

## Minimum telemetry (what MUST be logged)
- Model identifier + version hash
- Policy identifier + version
- Data provenance pointers (not raw sensitive content)
- Prompt/response fingerprints (redacted where needed)
- Human-in-the-loop overrides
- Actions executed (including external API calls)
- Errors, denials, and rate limits (machine-consumable)

---

## Runtime governance by posture (CSD)

### Control posture
- Local policy enforcement and local logging are mandatory.
- Rollback MUST be possible without provider permission.

### Steer posture
- Audit rights + telemetry access MUST be contractually enforceable.
- Model/provider changes MUST have notice and impact reports.

### Depend posture
- Managed dependence requires:
  - fallbacks,
  - exit drills,
  - resilience SLAs,
  - and evidence portability.

---

## Control mappings (SAM)
- `SAI-APP-AUD-02` Decision trace for high-impact workflows
- `SAI-MOD-AUD-01` Continuous evaluation + drift detection
- `SAI-APP-RED-01` Redress mechanism with trace-backed case handling
- `SAI-GOV-SEC-02` Incident taxonomy + reporting SLAs

# AI Infrastructure Resilience Playbook
## Energy–compute coupling stress tests and continuity drills

**Why this exists.** Energy and compute are coupled constraints. A sovereignty posture is only credible if it survives stress: outages, export controls, pricing shocks, and geopolitical discontinuities.

This playbook defines a repeatable set of drills and evidence expectations.

---

## Stress test suite (minimum)

### ST-1: Peak-load compute simulation
**Goal:** ensure mission-critical inference workloads hold under peak demand.
- Inputs: seasonal demand, event spikes, emergency conditions
- Outputs: latency distribution, error rates, capacity utilization
- Evidence: dashboards + incident report + corrective actions

### ST-2: Provider disruption scenario
**Goal:** validate continuity if a major provider is interrupted (policy, outage, sanctions, pricing shock).
- Demonstrate: fallback model path, workload migration, degraded-mode operation
- Evidence: time-to-failover, data integrity checks, service continuity metrics

### ST-3: Cross-border energy disruption scenario
**Goal:** validate compute continuity under grid stress or import disruption.
- Demonstrate: load shedding plan, AI energy zone relocation, priority scheduling
- Evidence: executed runbook, grid telemetry, post-event review

### ST-4: Export-control / chip supply shock tabletop
**Goal:** validate procurement resilience and medium-term capacity plans.
- Demonstrate: inventory, contract alternatives, strategic reserves, prioritization
- Evidence: updated sourcing plan + revised risk register

---

## Evidence pack (what “done” looks like)
- Runbook versions + change log
- Test execution logs + outcomes
- Observability dashboards snapshots
- Incident tickets and RCAs
- Updated posture declaration (if posture shifts)
- Updated SARI assessment

---

## Cadence (recommended)
- ST-1: quarterly for mission-critical services
- ST-2: semi-annual
- ST-3: annual (before peak season)
- ST-4: annual tabletop + mid-year update

---

## Control mappings (SAM)
- `SAI-CMP-RES-01` Domestic inference continuity for critical services
- `SAI-ENG-RES-01` AI demand forecasting integrated into grid planning
- `SAI-CMP-AUD-02` Retain failover traces and capacity reservation logs

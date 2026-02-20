# Paper analysis — Vision Paper: DPI-AI Framework 2026 (CDPI)

## 1. Architectural Primitives Extracted

- **Identity rails:** Implied via “public agents” and public-sector workflows; needs explicit binding to identity, delegation, and authority (who can act, on whose behalf, under what scope).
- **Data exchange layer:** Stronger: proposes **open and governed training data**, workflow templates, and interoperability patterns (including MCP). Treats data governance as a first-class layer.
- **AI capability layer:** Clear decomposition into **AI Blocks** (callable units), **safeguards as blocks**, and **DPI workflows** (orchestration). This is the right abstraction for “composable legitimacy”.
- **Governance assumptions:** Recognises oversight, auditability, and deployment inspection; still under-specifies tier triggers and redress SLAs.

## 2. Institutional Risk Surfaces

| Risk | Failure Mode | Likelihood | Impact | Priority |
|------|-------------|------------|--------|----------|
| Block sprawl without conformance | Everyone publishes “AI blocks” with inconsistent semantics; interoperability becomes chaos | High | High | P1 |
| Safeguards as decorative wrappers | Safeguard blocks exist but are optional/non-binding; Tier 2/3 workflows bypass them | Medium | High | P1 |
| Orchestration opacity | Workflow YAML becomes “shadow policy”; hard to audit why an outcome occurred | Medium | High | P1 |
| Agent authority creep | Public agents begin acting beyond advisory scope (Tier 1 → Tier 2/3 drift) | High | High | P1 |
| Model/data provenance gaps | Training and fine-tuning use unclear datasets; downstream harms untraceable | Medium | High | P2 |

## 3. Risk-to-Tier Mapping

Add explicit tier hooks into the workflow template:

- **Tier 0:** informational blocks only.
- **Tier 1:** draft/triage blocks with mandatory “human-confirm” gate.
- **Tier 2:** any eligibility/enforcement influence must emit a **contestable decision record**.
- **Tier 3:** automated action requires: **pre-deployment dossier + independent audit + kill switch + rollback + appeal path**.

## 4. Governance Binding

Recommended binding structure for the framework:

- **Controller obligations:** publish tiered workflow declarations; maintain decision logs; publish evaluation results; ensure redress pathways.
- **Block provider obligations:** signed responses for machine-consumed outputs; semantic versioning; clear I/O schemas; safety test attestations.
- **DPI operator controls:** registry + discovery controls; allowlisting; jurisdictional compute/data constraints; audit log retention.
- **Escalation pathways:** runtime triggers (drift, anomaly, complaint spikes, policy breach) → suspend block/workflow.

## 5. Standards Alignment

- **NIST AI RMF:** the “safeguards as callable blocks” maps cleanly to Measure/Manage, but needs evidence requirements.
- **OECD AI Principles:** supported via interoperability + transparency, but must be operationalised through conformance checklists.
- **ISO 42001:** fits as the management overlay; this paper can supply the “technical control plane” layer.
- **DPI building blocks:** strong alignment — this is essentially a DPI-native orchestration + registry approach for AI.

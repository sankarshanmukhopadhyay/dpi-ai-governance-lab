# DPI AI Ecosystem Threat Model

This threat model focuses on public-interest systems where harm can propagate through institutions, registries, agents, models and downstream effects rather than only through a single model decision.

For implementation and TRACE evaluation, use [Operational AI harms](operational-ai-harms.md). It converts the classes below into explicit causal chains with affected parties, observability, controls, redress and closure evidence.

## Threat and harm classes

### 1. Exclusion and wrongful denial

Identity mismatch, stale facts, inaccessible proof requirements or brittle thresholds deny or delay access to a service, entitlement or right.

### 2. Differential error and discriminatory burden

Model performance, data quality, proxy variables, policy design or operational process create uneven error, delay or proof burdens across affected groups.

TRACE should investigate disparity and mechanism without assuming a legal conclusion that belongs to the relevant jurisdiction and authority.

### 3. Automation bias and institutional de-skilling

Operators over-trust automated output, meaningful override authority disappears, or disagreement stops being recorded.

### 4. Governance capture and accountability diffusion

The institution or vendor running the system becomes the sole narrator of acceptable risk while responsibility for adverse outcomes fragments across agencies, vendors and technical components.

### 5. Population-scale and compounding harm

Small per-decision failure rates become material across high-volume public infrastructure, shared registries or dependent services. Single-case review can conceal clustered or cumulative harm.

### 6. Model, rule and orchestration drift

A model, threshold, policy rule, workflow or dependency changes after approval and deployed behavior no longer matches the declared governance state.

### 7. Data and provenance harm

Stale, incomplete, misattributed or untraceable facts become inputs to consequential decisions; training data, registry facts, policy rules or dependencies cannot be reconstructed.

### 8. Privacy, correlation and surveillance expansion

Identifiers, behavioral data, model telemetry or agent histories are reused across contexts, enabling linkage or purpose expansion beyond adopted governance bounds.

### 9. Authority and delegation abuse

An agent, service or operator acts without valid authority, exceeds delegated scope, continues after revocation, or obscures the accountable institution behind automation.

### 10. Manipulation, deception and synthetic evidence

Forged documents, synthetic media, prompt manipulation, misleading model output or fabricated evidence affects a consequential decision without sufficient provenance or integrity controls.

### 11. Security and supply-chain induced harm

Compromised dependencies, poisoned data, model swaps, stolen credentials or malicious tools alter decisions, evidence or effects.

### 12. Remedy and correction propagation failure

Appeal exists on paper but cannot produce effective remedy, or a corrected fact/decision fails to invalidate, recompute, replace or compensate mandatory downstream effects.

## Signals worth watching

Prefer evidence-bearing indicators such as:

- sudden change in override, denial, referral or escalation rate;
- complaint/appeal clusters by geography, channel or relevant proxy;
- materially elevated appeal reversal rates;
- subgroup differences in error, delay or proof burden;
- repeated use of superseded facts or decisions;
- mismatch between approved and deployed model/rule versions;
- action after delegation revocation or expiry;
- inconsistent acceptance of the same evidence across relying institutions;
- unresolved mandatory correction targets;
- unusual cross-service access or correlation patterns;
- dependency/artifact integrity mismatch;
- excessive delay between incident discovery, correction and effective remedy.

## Control posture

A DPI/AI threat model should connect each material threat to:

1. the affected party and experienced harm;
2. the technical/institutional mechanism;
3. accountable authority and any delegation failure;
4. preventive, detective and corrective controls;
5. observable signals and evidence sources;
6. effective redress/remedy;
7. closure evidence and residual risk.

Use `schemas/harms/harm-chain.schema.json`, `templates/harm-chain-template.yaml` and `templates/harm-chain.example.yaml` to make that structure reusable and machine-verifiable.

A threat catalogue that cannot say how harm is detected, stopped, corrected and evidenced is useful for discussion but insufficient for executable governance.

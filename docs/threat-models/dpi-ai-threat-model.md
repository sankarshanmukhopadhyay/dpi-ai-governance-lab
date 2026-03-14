# DPI AI Ecosystem Threat Model

This threat model focuses on public-interest systems where harm can propagate through institutions, registries, and eligibility flows rather than only through a single model decision.

## Threat classes

### 1. Exclusion and access denial
People are incorrectly denied access because identity matching, data quality, or decision thresholds encode brittle assumptions.

### 2. Automation bias
Frontline operators over-trust outputs and stop exercising judgement, even when signals are weak or contradictory.

### 3. Governance capture
The institution running the system becomes the sole narrator of risk, performance, and acceptable error, leaving affected populations without effective challenge pathways.

### 4. Population-scale drift
A model or rulebook shifts over time and creates aggregate harm that is invisible in isolated case review.

### 5. Data lineage opacity
The provenance of training data, policy rules, or external dependencies cannot be reconstructed during review or appeal.

### 6. Remedy failure
Notice exists on paper, but users cannot realistically understand, contest, or reverse harmful outcomes.

## Signals worth watching

- Sudden changes in override rate
- Complaint clusters by geography or demographic proxy
- Appeals that reverse decisions at materially higher rates than frontline review
- Latency between incident identification and corrective action
- Persistent mismatch between declared policy and deployed behavior

## Control posture

A sane DPI deployment SHOULD pair threat identification with controls, evidence, and explicit redress channels. Threat models that stop at attack trees but ignore institutional asymmetry are decorative wallpaper. Nice wallpaper, perhaps. Still wallpaper.

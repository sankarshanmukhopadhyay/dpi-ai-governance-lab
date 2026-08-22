# TRACE review — The Digital Constitution of the State

## Evaluation stance

The essay argues that shared digital systems become functionally constitutional when they shape recognition, authority, accountability and remedy. TRACE tests what system-level contracts are needed to make those constitutional properties independently verifiable.

## Strong implementation signals

The essay explicitly distinguishes logs from reconstruction, identifies probabilistic matching as an exercise of public power rather than a neutral technical step, and asks whether people can challenge data, matching logic or thresholds. It also preserves human review for ambiguous cases.

## Material implementation-distance findings

### 1. Probabilistic matching requires inference traceability

The essay recognizes that matching thresholds and confidence scores can determine exclusion, but an operator needs a machine-readable trace binding algorithm/model identity, version, input snapshot, threshold and output to the consequential decision.

Required capability: `CAP-INFERENCE-TRACEABILITY`.

### 2. Constitutional remedy needs an executable appeal path

The essay treats remedy as a constitutional property and asks whether affected people can challenge data, matches and thresholds. Deployment still requires a redress authority, lifecycle, timing, correction/remedy outputs and evidence that the route works.

Required capability: `CAP-REDRESS-APPEAL`.

### 3. Role-separated public power needs bounded delegated execution

The architecture requires separation of powers in systems, but consequential execution by services or automated components still needs explicit authority scope, validity, revocation and runtime authorization evidence.

Required capability: `CAP-AUTHORITY-BOUNDED-DELEGATION`.

## Overall assessment

The essay provides one of the strongest source-level statements in the corpus about why inference, traceability and remedy are governance rather than technical details. The remaining implementation distance is converting those principles into portable runtime evidence contracts.

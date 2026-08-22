# TRACE review — The Minimum Digital Kernel of an Unbundled State

## Evaluation stance

The essay already behaves like a proto-specification: it names authority directories, rulebooks, registries, decision traces, evidence, appeals and audit. TRACE therefore focuses on the remaining interfaces needed for independent implementation and verification.

## Strong implementation signals

The essay makes the decision receipt central and binds it to authority, rule version, facts, checks, reason codes and remedy. It also assigns distinct institutional responsibilities and treats correction/recomputation as part of fairness rather than as an afterthought.

## Material implementation-distance findings

### 1. Certified authority needs bounded machine delegation

A directory can show that an institution or provider is recognized, but a runtime service still needs an explicit delegation envelope stating what the delegate may do, to which resources, for which purpose, during which validity period, and how revocation affects pending effects.

Required capability: `CAP-AUTHORITY-BOUNDED-DELEGATION`.

### 2. Reconstructability must bind the inference step

The signed decision trace identifies rules, facts and outcomes, but automated or AI-assisted decisions also need a verifiable account of the transformation between inputs and outcome: model or inference identity, version, thresholds/parameters where relevant, and the relationship between probabilistic output and the normative rule.

Required capability: `CAP-INFERENCE-TRACEABILITY`.

### 3. Correction must propagate as an executable lifecycle

The essay requires corrected facts to trigger recomputation, but an operator still needs dependency discovery, propagation targets, partial-failure semantics, acknowledgements, downstream invalidation/recomputation and completion evidence.

Required capability: `CAP-CORRECTION-PROPAGATION`.

## Overall assessment

The Minimum Digital Kernel is already unusually close to an implementation architecture. The remaining gaps are principally runtime delegation, inference binding and the state machine that turns a successful correction into evidence-backed downstream change.

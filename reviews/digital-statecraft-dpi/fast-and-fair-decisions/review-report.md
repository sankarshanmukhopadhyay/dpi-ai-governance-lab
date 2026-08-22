# TRACE review — Making Fast and Fair Decisions in the Age of AI

## Evaluation stance

The essay is strongly operational: it separates five institutional roles and defines shared objects for rules, facts, decision receipts and corrections. TRACE focuses on whether those objects and role boundaries can be independently enforced and evidenced at runtime.

## Strong implementation signals

The essay explicitly rejects explainability as merely a model property, distinguishes normative rules from probabilistic models, requires immutable/versioned rules, and makes correction an architectural condition for safe speed. It also recognizes that a decision receipt is weak if the same institution controls rule, fact, decision and appeal.

## Material implementation-distance findings

### 1. Certified operators require bounded delegated authority

The Operator is described as a certified institution, but certification alone does not state the machine-enforceable scope, validity, revocation and effect authorization applicable to a specific service or automated actor.

Required capability: `CAP-AUTHORITY-BOUNDED-DELEGATION`.

### 2. Rule/model separation needs a portable inference trace

The essay correctly says a risk score or classification is not the rule. To make that distinction enforceable later, the decision evidence needs an immutable record of which model/inference version, inputs, thresholds and outputs contributed to the decision and how the normative rule used them.

Required capability: `CAP-INFERENCE-TRACEABILITY`.

### 3. Correction must propagate beyond the appeal decision

A successful appeal can order facts corrected and decisions recomputed. Operators still need a protocol for finding dependent decisions, propagating correction, handling partial failure, superseding prior outputs and proving completion.

Required capability: `CAP-CORRECTION-PROPAGATION`.

### 4. Systemic audit claims need closure evidence

The Audit Authority is expected to detect patterns across decisions, but an implementation needs a reproducible evidence bundle tying the relevant control claim to decision records, negative tests, corrective actions and verification outcomes.

Required capability: `CAP-EVIDENCE-CLOSURE`.

## Overall assessment

This is one of the most implementation-ready pieces in the corpus. TRACE mostly identifies serialization and lifecycle gaps needed to turn its strong institutional design into portable, testable governance interfaces.

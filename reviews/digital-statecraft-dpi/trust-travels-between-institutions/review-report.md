# TRACE review — How Trust Travels Between Institutions

## Evaluation stance

The essay explicitly distinguishes authenticity, authority, admissibility and accountability. TRACE therefore focuses on turning those institutional trust relationships into portable reliance and correction contracts that a receiving institution can execute and later audit.

## Strong implementation signals

This is the corpus's strongest articulation of the boundary between verification and reliance. It correctly states that credentials are carriers of upstream decisions, that admissibility is a property of institutional relationships rather than cryptography alone, and that accountability requires institutions able to hear grievances, impose consequence and propagate correction.

## Material implementation-distance findings

### 1. Admissibility needs a machine-readable reliance decision

The essay provides the conceptual test for admissibility but an operator still needs a portable profile stating which upstream authority/output can be relied upon for which downstream decision, purpose, jurisdiction and conditions, including validity, liability/recourse and revocation.

Required capability: `CAP-INTERINSTITUTIONAL-ADMISSIBILITY`.

### 2. Correction propagation needs an executable protocol

The essay explicitly asks whether correction propagates through downstream decisions that relied on the original output. Implementation requires dependency discovery, invalidation/recomputation, acknowledgement, partial-failure handling and completion evidence.

Required capability: `CAP-CORRECTION-PROPAGATION`.

### 3. Accountability needs evidence-backed closure

The four-layer framework culminates in institutions that can correct, hear grievance, impose liability and order remedy. An assurance process still needs versioned evidence demonstrating that these controls worked for the relevant reliance chain.

Required capability: `CAP-EVIDENCE-CLOSURE`.

## Overall assessment

The essay supplies a strong theory of why technically verifiable objects may still fail to cross institutional boundaries. The key implementation contribution for the repository programme is to make admissibility and downstream correction explicit, testable objects rather than implicit institutional understandings.

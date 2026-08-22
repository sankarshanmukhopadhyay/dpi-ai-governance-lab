# TRACE review — The Governance Stack

## Evaluation stance

The essay supplies a layered architecture for norms, institutions, decision protocols, DPI rails and applications. TRACE tests the interfaces between those layers: where authority crosses boundaries, how decisions remain reconstructable, and what evidence proves that governance controls actually worked.

## Strong implementation signals

The essay correctly treats architecture as part of governance, identifies distinct responsibilities by layer, and makes contestability and decision structure part of the shared kernel rather than an application-specific afterthought. It also names concentration, exclusion, surveillance and fragmentation risks by layer.

## Material implementation-distance findings

### 1. Cross-layer authority needs enforceable handoff semantics

The stack says institutions allocate authority and the kernel structures decisions, but an implementer still needs a bounded delegation/authorization contract when institutional authority is exercised by a kernel service, rail, vendor-operated component or automated actor.

Required capability: `CAP-AUTHORITY-BOUNDED-DELEGATION`.

### 2. The decision object needs an inference trace

A structured rule/evidence/authority/outcome object is not fully reconstructable where matching logic, scoring, classification or another automated transformation materially contributes to the result. The transformation itself must be versioned and evidence-bound.

Required capability: `CAP-INFERENCE-TRACEABILITY`.

### 3. Assurance needs closure evidence, not architecture alone

The stack identifies layer-specific risks and oversight needs but does not define the evidence package by which an operator proves that required controls, negative paths and corrective actions were actually exercised.

Required capability: `CAP-EVIDENCE-CLOSURE`.

## Overall assessment

The layered model is strong as an analytical and design frame. The principal implementation distance lies at the interfaces: delegated authority across layers, reconstructing automated transformations, and producing evidence that governance guarantees hold in operation.

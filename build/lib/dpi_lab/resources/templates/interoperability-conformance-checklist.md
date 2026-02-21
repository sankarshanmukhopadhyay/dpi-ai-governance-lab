# Interoperability Conformance Checklist (ELP)
Use this checklist to validate that a system provides **exit leverage** and does not hard-wire dependence.

## A. Data portability
- [ ] Export supported in documented, widely used formats.
- [ ] Export includes schema versions + lineage metadata.
- [ ] Extraction completes within a defined SLA for mission-critical datasets.
- [ ] Deletion requests have verifiable completion evidence.

## B. Model portability
- [ ] Vendor-neutral orchestration interface exists.
- [ ] At least two runtime targets are supported and tested.
- [ ] Model swap preserves policy enforcement and logging.

## C. API compatibility
- [ ] APIs are versioned; backward compatibility window is defined.
- [ ] Breaking changes provide migration tools + timelines.
- [ ] Interface specifications are published to implementers.

## D. Workload migration drills
- [ ] Annual exit drill executed for mission-critical workload(s).
- [ ] Drill captures time-to-migrate, integrity checks, performance deltas.
- [ ] Corrective actions are tracked to closure.

## E. Contractual exit rights
- [ ] Audit rights defined and enforceable.
- [ ] Non-interruption clause for critical services.
- [ ] Data export + deletion rights.
- [ ] Knowledge transfer / embedded support obligations.
- [ ] Exit assistance and pricing are explicit.

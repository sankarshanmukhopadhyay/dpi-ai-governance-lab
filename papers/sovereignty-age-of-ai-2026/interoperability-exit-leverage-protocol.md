# Exit Leverage Protocol (ELP)
## Interoperability as strategic autonomy (not an engineering nicety)

**Problem.** “Interoperability” is often treated as hygiene. In sovereignty terms it is **exit leverage**:
the ability to switch providers, swap models, migrate workloads, and preserve institutional continuity without a rewrite.

**Principle.** If you cannot exit, you do not control. You rent.

---

## ELP requirements (normative)

### ELP-1: Data portability MUST be provable
- Systems MUST support export in documented, widely used formats.
- Exports MUST include lineage + schema versions.
- Data deletion requests MUST have verifiable completion evidence.

### ELP-2: Model portability MUST be supported
- Model interfaces MUST be vendor-neutral at the orchestration layer.
- A minimum of two compliant runtime targets MUST be supported (e.g., provider A + provider B, or cloud + on-prem).
- Model swap MUST preserve policy constraints and logging.

### ELP-3: API compatibility MUST be stable
- Public APIs MUST be versioned and backward compatible within defined windows.
- Breaking changes MUST provide migration tools and timelines.

### ELP-4: Workload migration MUST be rehearsed
- Annual “exit drill” MUST be executed for mission-critical systems.
- Drill evidence MUST include: time-to-migrate, data integrity checks, performance deltas, incident logs.

### ELP-5: Procurement MUST encode exit rights
Contracts MUST include:
- audit rights
- non-interruption clauses for critical services
- data export and deletion rights
- escrow / fallback provisions (where appropriate)
- documented exit assistance and knowledge transfer

---

## Conformance checklist
Use: `templates/interoperability-conformance-checklist.md`

---

## Control mappings
- `SAI-CMP-INT-03` Portability across compliant runtimes
- `SAI-APP-INT-03` Open APIs + vendor-neutral orchestration
- `SAI-DAT-AUD-02` Lineage + provenance for exported datasets

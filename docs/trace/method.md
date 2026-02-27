# TRACE Method

TRACE is a **layered evaluation** method that treats DPI–AI governance as an **operational system** with observable properties.

## Core lenses

TRACE evaluates a target across four lenses:

1. **Trust** — identity, authority, accountability, transparency, and dispute/appeal capability.
2. **Risk** — risk identification, tiering, controls, monitoring, incident response, and residual risk acceptance.
3. **Architecture** — interoperability, dependency surfaces, data flows, security boundaries, and survivability under pressure.
4. **Conformance** — stated requirements vs implemented mechanisms; evidence quality; auditability; repeatability.


## Identity Legitimacy checkpoint (mandatory)

TRACE treats **identity legitimacy** as a *required checkpoint* (not a separate axis). Reviewers MUST explicitly evaluate:

- **Assurance level**: what baseline is used (e.g., ANAB) and what minimum level is required for the deployment’s risk tier
- **Delegation clarity**: who granted authority to act, and how that delegation is bound and reviewable
- **Revocation semantics**: how identities/authorizations are suspended or revoked, and how relying parties learn about it
- **Registry transparency**: where the authoritative record lives and how integrity is maintained

Implementation note: TRACE SHOULD reference external identity assurance baselines rather than duplicating their annex sets. See: `docs/adr/adr-trace-identity-legitimacy.md`.

## Workflow

1. **Scope & context**
   - Define system boundary, actors, decision rights, and operational environment.
2. **Extract & normalize**
   - Convert source material into canonical text + hashes.
3. **Assess**
   - Apply TRACE controls; capture findings and evidence gaps.
4. **Score**
   - Produce a scorecard (rubric + confidence).
5. **Recommend**
   - Convert findings into a prioritized remediation backlog (quick wins vs structural changes).
6. **Validate**
   - Run schema checks and consistency checks to reduce “governance theatre”.

## Output contract

A TRACE evaluation is complete when the required outputs exist and are internally consistent:

- `paper-analysis.md`
- `paper-review-report.md`
- `paper-review-metadata.yaml`
- `paper-review-scorecard.yaml`

(Names may vary outside paper reviews; the contract is the structure.)

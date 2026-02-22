# TRACE Method

TRACE is a **layered evaluation** method that treats DPI–AI governance as an **operational system** with observable properties.

## Core lenses

TRACE evaluates a target across four lenses:

1. **Trust** — identity, authority, accountability, transparency, and dispute/appeal capability.
2. **Risk** — risk identification, tiering, controls, monitoring, incident response, and residual risk acceptance.
3. **Architecture** — interoperability, dependency surfaces, data flows, security boundaries, and survivability under pressure.
4. **Conformance** — stated requirements vs implemented mechanisms; evidence quality; auditability; repeatability.

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

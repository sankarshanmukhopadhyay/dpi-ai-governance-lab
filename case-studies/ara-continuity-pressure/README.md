---
layout: default
title: ARA continuity pressure test
nav_order: 10
---

# ARA continuity pressure test

This case asks whether the Lab's five-state assessment-continuity model survives contact with an independently developed trust-system evidence surface without adding ARA-specific lifecycle logic.

## External source

The pressure source is Trust Protocol Interop Lab case `IC-ARA-REL-001`, pinned at repository commit:

`8e50e48cf6ec14526a72e13850020a981866eb83`

The local `source-baseline.yaml` records the exact source artifacts and Git blob identifiers used.

The source case already establishes several temporal propositions relevant to this test:

- current authority is distinct from identity or capability possession;
- stale or revoked authority cannot authorize a new material act;
- missing authority evidence is not PASS;
- historical state is preserved rather than overwritten;
- later revocation changes present consequences without rewriting historically legitimate actions.

## Bounded mapping

`evidence-map.yaml` maps only source propositions that correspond to the existing `CAP-AUTHORITY-BOUNDED-DELEGATION-1` requirements.

The mapping does **not** claim:

- that ARA implements the DPI/AI Governance profile;
- protocol or standards equivalence;
- legal validity;
- production assurance;
- certification.

It asks only whether independently produced evidence can satisfy the technical propositions needed to pressure the continuity model.

## Result

The same state vocabulary survives unchanged:

| ARA-native condition | Existing state |
| --- | --- |
| no material change after assessment | `valid` |
| authority revoked | `invalidated` |
| current role/delegation scope changes | `reassessment_required` |
| fresh later assessment replaces prior result | `superseded` |
| current authority status unavailable | `indeterminate` |

No sixth state and no ARA-specific precedence rule are required.

## Important temporal finding

ARA's own lifecycle judgment says that later revocation must not invalidate previously legitimate historical actions. The continuity model preserves this directly: the original assessment remains a historical PASS while its present reliance state can become `invalidated`.

That is the strongest result of this pressure test because it is independently derived in the source system rather than invented for the DPI/AI Governance fixture.

## Machine-verifiable surfaces

- `source-baseline.yaml`
- `evidence-map.yaml`
- `assessment-pass.yaml`
- `continuity-*.yaml`
- the existing generic assurance and continuity validators

## Claim boundary

This is a cross-system pressure test of the lifecycle state model. It is not an assurance judgment over ARPA, ARA as a standard, or any production agent system.

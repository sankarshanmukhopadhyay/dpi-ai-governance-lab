---
layout: default
title: Delegated entitlement closure fixture
parent: Evaluations
nav_order: 4
---

# Delegated entitlement closure fixture

This experimental fixture demonstrates the full operator loop for `CAP-AUTHORITY-BOUNDED-DELEGATION`: identify a governance gap, instantiate standardized remediation, execute failure paths, preserve authorization evidence, and produce evidence sufficient for a TRACE closure decision within the fixture scope.

{: .warning }
This is a jurisdiction-neutral test fixture. Closing the fixture gap does not close any real publication review, confer legal authority, or certify a production deployment.

## End-to-end flow

```mermaid
flowchart LR
    G[TRACE gap: bounded delegation missing] --> R[Resolve standardized remediation]
    R --> D[Instantiate delegation record]
    D --> T[Execute positive and negative requests]
    T --> A[Produce runtime authorization records]
    A --> E[Bind allowed effect to authorization]
    E --> C{Closure criteria}
    C -->|pass| X[Fixture gap closed]
    C -->|fail| O[Gap remains open]
```

## Actors and authority

```mermaid
sequenceDiagram
    participant PA as Programme authority
    participant Agent as Service agent
    participant Gate as Policy decision point
    participant Pay as Payment service
    participant Appeal as Appeals office
    PA->>Agent: bounded delegation
    Agent->>Gate: payment request + delegation
    Gate->>Gate: evaluate status, time and scope
    alt valid delegation
        Gate-->>Agent: allow + AUTHZ id
        Agent->>Pay: execute with AUTHZ id
        Pay-->>Gate: effect id correlated
    else revoked/expired/out of scope
        Gate-->>Agent: deny + reason code
    end
    Appeal-->>PA: independent redress/remedy path retained
```

## Fixture artifacts

- `delegation-record.yaml` — instantiated bounded delegation.
- `authorization-requests.yaml` — positive and adversarial requests with expected decisions.
- `runtime-authorization-records.yaml` — preserved decision evidence.
- `closure-evidence.yaml` — control-to-evidence mapping and closure result.

## Closure claim

The fixture claims only that its own acceptance criteria are satisfied:

1. a named accountable authority exists;
2. delegation is bounded by actor, action, resource, purpose and time;
3. revoked, expired and out-of-scope requests fail closed;
4. the allowed payment effect is correlated to its runtime authorization;
5. redress remains discoverable; and
6. the evidence set records the result.

The intended programme consequence is methodological: TRACE can now demonstrate **evidence-backed closure in a realistic synthetic deployment fixture**, while the real-review baseline remains historically unchanged at zero deployment-backed closures.

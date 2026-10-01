---
layout: default
title: TRQP temporal continuity pressure test
nav_order: 11
---

# TRQP temporal continuity pressure test

This case tests whether the five-state assurance-continuity model survives a non-delegation, evidence-centric domain: TRQP current/request-time semantics and historical-state answerability.

## Source boundary

The source repository is pinned at:

`009c589ffa4e3098c7700a19b007505d6a29c30a`

The source supports three distinct facts relevant here:

1. authorization queries can carry a requested `context.time`;
2. authorization responses expose `time_requested` and `time_evaluated`;
3. the downstream authority-at-commitment assessment explicitly says current state and historical state must remain distinct and that no general historical/as-of authorization contract is established by the current core.

Those facts do **not** prove that an implementation can reconstruct arbitrary historical effective state.

## Pressure profile

Unlike the earlier ARA test, this case does not reuse bounded delegation. It uses the existing `CAP-EVIDENCE-CLOSURE` capability and its evidence-centric conformance profile.

The assessment asks whether the temporal claims are:

- version-bound;
- provenance/integrity-bound;
- mapped from claims to supporting source evidence;
- verified with an explicit result that preserves evidence gaps.

## Five-state result

| Temporal/evidence condition | Existing state |
| --- | --- |
| no new material information | `valid` |
| governing rule materially changes | `reassessment_required` |
| later authoritative evidence contradicts a mandatory basis | `invalidated` |
| historical effective state cannot be reconstructed | `indeterminate` |
| a later assessment explicitly replaces the earlier closure | `superseded` |

No sixth state is required.

## Historical validity versus present reliance

The difficult case is historical reconstruction.

A prior response can remain an attributable historical artifact, including its `time_requested` and `time_evaluated`, while a later verifier is unable to establish the historically applicable effective state. The model does not need a state such as `historically_valid_but_currently_unreliable`.

Instead:

```text
historical assessment record = unchanged
present continuity state      = indeterminate
```

If later authoritative evidence actually contradicts a mandatory basis, present reliance becomes `invalidated` instead.

This preserves the distinction between:

- historical observation;
- historical effective state;
- present determination about historical state.

## Claim boundary

This test does not amend TRQP, assert a general historical-query capability, or decide what an authoritative registry must persist internally. It demonstrates only that the existing five-state continuity vocabulary can represent the source-supported temporal evidence conditions without TRQP-specific controller logic.

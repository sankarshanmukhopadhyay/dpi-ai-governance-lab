---
layout: default
title: "TRACE — Trust, Risk, Architecture & Conformance Evaluation"
nav_order: 2
permalink: /trace/
---

# TRACE — Trust, Risk, Architecture & Conformance Evaluation

**TRACE (Trust, Risk, Architecture & Conformance Evaluation)** is the DPI–AI Governance Lab's named method for assessing systems, programmes, policies, and implementation propositions as **operational governance systems with observable properties**.

TRACE is designed to produce **auditable outputs, actionable governance gaps, implementation requirements, and evidence-backed closure assessments** rather than aspirational principles or an unsupported compliance label.

This page is the canonical reader-facing introduction to TRACE. Detailed controls, scoring rules, schemas, templates, fixtures, and worked evaluations remain authoritative in their repository locations.

## Why TRACE exists

Important governance propositions are often expressed as prose:

- an authority should be accountable;
- a delegated actor should operate within scope;
- an appeal should exist;
- a system should be transparent;
- a control should reduce risk;
- an implementation should conform to a declared policy or architecture.

Those propositions are difficult to rely on if nobody can show:

1. **what exactly must be true;**
2. **where authority comes from and where it ends;**
3. **what evidence supports the proposition;**
4. **how an implementation can be tested;**
5. **what happens when evidence is missing or contradictory;**
6. **what remediation would close a material gap; and**
7. **whether closure survives re-evaluation.**

TRACE provides a repeatable way to move from a governance proposition to evidence, gaps, remediation requirements, implementation tests, and a bounded conclusion.

```text
publication / system proposition / deployment
        ↓
TRACE evaluation
        ↓
evidence-backed finding
        ↓
normalized governance gap
        ↓
required capability
        ↓
remediation
        ↓
implementation
        ↓
negative tests + evidence
        ↓
TRACE re-evaluation
        ↓
closure / residual risk
```

## What TRACE evaluates

TRACE applies four complementary lenses.

### 1. Trust

Trust asks whether reliance is justified by explicit authority and accountability rather than assumption.

Typical questions include:

- Who is authorized to act?
- What is the source and scope of that authority?
- Is delegation explicit and bounded?
- Can authority be suspended or revoked?
- Is there a responsible party for consequential decisions?
- Are transparency, challenge, correction, and appeal pathways operational?

### 2. Risk

Risk asks whether material failure modes are identified, controlled, observed, and accepted by an appropriate authority.

Typical questions include:

- What can fail and who is affected?
- How is risk tiered or prioritized?
- What controls address the risk?
- How is control effectiveness observed?
- What residual risk remains?
- Who has authority to accept that residual risk?

### 3. Architecture

Architecture asks whether the proposed governance model can survive real system boundaries and dependencies.

Typical questions include:

- Where are the trust and security boundaries?
- What dependencies, registries, data flows, services, models, or institutions are relied upon?
- What happens when a dependency is stale, unavailable, compromised, or inconsistent?
- Can state changes, revocation, correction, and remediation propagate?
- Are interoperability assumptions explicit?

### 4. Conformance

Conformance asks whether stated requirements are actually represented by implemented mechanisms and evidence.

Typical questions include:

- What requirement is being tested?
- What implementation mechanism is intended to satisfy it?
- What evidence demonstrates that mechanism is present and effective?
- Can another reviewer reproduce the conclusion?
- What evidence would falsify the claim?
- Does missing evidence remain visibly missing rather than becoming a pass?

## Mandatory identity-legitimacy checkpoint

TRACE treats **identity legitimacy as a required checkpoint, not a separate fifth axis**.

An evaluation must explicitly consider:

- the applicable identity/assurance baseline;
- who granted authority to act;
- how delegation is bound, limited, and reviewable;
- revocation and suspension semantics;
- the authoritative record or registry and its integrity assumptions.

TRACE should reference appropriate external identity-assurance baselines rather than duplicate them. The repository's architectural decision record on this point remains authoritative.

## What TRACE produces

A complete TRACE evaluation is intended to leave an inspectable evidence trail rather than only a narrative opinion.

Depending on the evaluation path, outputs include:

- a **TRACE report** with scope, findings, reasoning, recommendations, and limitations;
- a **scorecard** using the repository's defined scoring model;
- **evidence references** identifying what supports each material finding;
- **control mappings** showing what was assessed against what;
- a machine-readable **governance-gap register** where material implementation gaps are normalized;
- required **CAP-*** capability statements for remediation;
- implementation and negative-test evidence where closure is being assessed;
- a re-evaluation result that distinguishes verified closure from residual or indeterminate risk.

A score, finding, mapping, or available remediation artifact is not by itself proof that a real deployment is safe or compliant.

## Evidence discipline

TRACE separates a proposition from the evidence that supports it.

For every material conclusion, the evaluator should be able to answer:

```text
What is the claim?
        ↓
What source or system evidence supports it?
        ↓
Is that evidence explicit, inferred, missing, stale, or contradictory?
        ↓
What governance gap remains?
        ↓
What evidence would demonstrate closure?
```

The stable evaluation contract requires evidence-linked findings, stated scope and assumptions, explicit limitations, and traceability to source material. When evidence is insufficient, uncertainty remains visible.

This is a core TRACE property: **absence of evidence is not converted into assurance.**

## How to apply TRACE

TRACE supports more than one starting point.

### Path A — Evaluate a publication or policy proposition

Use this path when the source is a paper, policy, framework, proposal, or architecture document.

1. **Scope the evaluation.** Identify the source, system boundary, actors, decision rights, and declared assumptions.
2. **Extract and preserve evidence.** Retain stable source references and provenance.
3. **Apply TRACE.** Evaluate material propositions through the four lenses and mandatory checkpoint.
4. **Record findings.** Distinguish explicit source claims from evaluator inference.
5. **Normalize material gaps.** Convert important findings into implementation-relevant governance gaps.
6. **Identify required capabilities.** Express what an implementer would need in order to close the gap.
7. **Map or design remediation.** Reuse existing remediation where justified; do not create artifacts merely to improve coverage.
8. **Verify closure where possible.** Test implementation and failure paths.
9. **Re-evaluate.** Record what changed, what remains open, and what evidence supports closure.

### Path B — Start from an implementation idea

Use this path when a team already has a service, product, agent, registry interaction, eligibility process, AI-assisted decision, or other system proposition.

Begin by making explicit:

1. consequential decisions and effects;
2. accountable authorities and delegates;
3. facts, rules, model outputs, credentials, or evidence inputs;
4. governance failure paths;
5. required governance capabilities;
6. enforcement points;
7. closure evidence.

The repository's [implementation-first guide](../implementation-first.md) provides the detailed workflow.

### Path C — Improve an existing deployment

Use the [operator playbook](../operator-playbook.md) to move from an observed weakness to a normalized capability requirement, remediation, implementation, test, evidence, and re-evaluation.

## Minimum viable implementation

A team can adopt TRACE without adopting every repository artifact.

A minimum useful implementation should:

1. define the evaluation target and boundary;
2. identify relevant actors, authorities, delegations, and consequential decisions;
3. evaluate the target through Trust, Risk, Architecture, and Conformance;
4. preserve evidence references for material findings;
5. distinguish explicit evidence, inference, missing evidence, and uncertainty;
6. create actionable remediation requirements for material gaps;
7. define what evidence would demonstrate closure; and
8. re-evaluate after remediation.

A repeatable implementation should additionally use the repository's stable evaluation contract, schemas, scorecards, CLI validation, governance-gap model, and reusable remediation artifacts.

An automated or high-assurance implementation should connect those outputs to executable tests, machine-readable evidence, and lifecycle-aware assurance.

## Worked implementation model

A useful TRACE result is not:

```text
"Appeal is important."
```

It is closer to:

```text
Proposition:
A consequential eligibility decision can be challenged.

TRACE finding:
The design describes human review but does not identify
the authority, request contract, status lifecycle, correction
propagation, or closure evidence.

Governance gap:
Operational appeal and remedy are underspecified.

Required capability:
The system needs a bounded appeal workflow with a responsible
authority, decision reference, status transitions, correction/
remediation behavior, and evidence of outcome.

Implementation evidence:
Negative-path tests demonstrate that an appeal can be opened,
cannot be silently discarded, produces a review outcome, and
propagates an accepted correction to affected downstream state.

Re-evaluation:
Closed within the tested scope; residual deployment and
institutional-authority assumptions remain explicit.
```

The point is not the example domain. The point is the transformation from **governance language to a falsifiable operational proposition**.

## Relationship to remediation artifacts

The DPI–AI Governance Lab and the companion DPI–AI Governance Artifacts repository have deliberately separate responsibilities.

**The Lab owns:**

- TRACE evaluation;
- evidence extraction;
- finding and gap normalization;
- comparison and recurring-gap analysis;
- verification;
- scoped closure assessment.

**The Artifacts repository owns:**

- reusable remediation schemas;
- controlled implementation guidance;
- test vectors;
- implementation patterns;
- evidence requirements.

**Adopting organizations retain:**

- legal authority;
- institutional authority;
- procurement authority;
- programme authority;
- deployment decisions;
- risk acceptance.

TRACE can evaluate a proposition and the evidence for it. It does not acquire the authority to make the underlying public, legal, institutional, or business decision.

## Relationship to TSAM

TRACE and the **Trust Systems Assurance Method (TSAM)** operate at different abstraction layers.

- **TRACE defines governance analysis:** what must be governed, why it matters, what is missing, and what evidence is needed.
- **TSAM defines assurance implementation discipline:** how governance intent is bound to assurance levels, conformance verification, runtime integrity controls, and evidence/observability.

Where both are used:

```text
TRACE
governance analysis
        ↓
risk / authority / redress / architecture requirements
        ↓
TSAM
assurance engineering
        ↓
controls → verification → runtime integrity → evidence
```

TRACE does not prescribe a specific technical enforcement mechanism. TSAM does not redefine governance legitimacy.

See [TRACE ↔ TSAM](TRACE-TSAM.md) for the repository-local relationship pointer and the canonical relationship source identified there.

## Business and operational value

TRACE is intended to improve the economics and quality of governance work by making important uncertainty visible earlier and making closure demonstrable.

| Common condition | TRACE contribution |
| --- | --- |
| Governance intent is spread across prose and meetings | Converts material propositions into a repeatable evaluation and evidence trail |
| Implementation gaps emerge late | Identifies missing authority, lifecycle, evidence, redress, or architecture requirements before they become hidden deployment assumptions |
| Reviews vary substantially by reviewer | Uses a stable method, scoring model, evidence contract, and reproducible outputs |
| Remediation is described only narratively | Converts material gaps into explicit capability and evidence requirements |
| Controls exist but their effectiveness is unclear | Connects governance claims to implementation and negative-path evidence |
| Audit or assurance requires retrospective reconstruction | Preserves evidence and reasoning as part of the evaluation lifecycle |
| Closure is asserted after a fix | Requires defined closure evidence and re-evaluation |
| Unknown or missing information is treated optimistically | Keeps uncertainty and evidence gaps explicit |

The practical value is therefore not a generic promise to "increase trust." TRACE aims to **reduce the cost of discovering governance failure, make remediation more precise, and make important governance claims easier to review, challenge, test, and re-evaluate.**

Actual financial, compliance, safety, or delivery outcomes remain deployment-specific and must be evidenced by the adopting organization.

## What TRACE does not claim

TRACE is not:

- a legal compliance determination;
- a certification or accreditation programme;
- an assertion that a source publication is correct or incorrect;
- a substitute for the responsible institution's authority or risk acceptance;
- a guarantee that a deployed system is safe merely because a review is complete;
- a requirement that every publication contain implementation detail outside its intended scope.

A missing implementation detail is not automatically a defect. TRACE asks a narrower question: **if an implementer relies on this proposition, what must still be defined, implemented, tested, evidenced, or governed?**

## Maturity and versioning

TRACE is versioned independently from the Lab workbench.

- The current TRACE method version is recorded in `TRACE_VERSION`.
- The repository's stable review spine is defined in `methodology/`.
- Methodology changes follow the repository's governance and change-control rules.
- Compatibility with companion artifacts is recorded separately.

Consumers requiring reproducible evaluation should record the TRACE version and relevant rubric or contract versions used.

## Implementation and reference links

Start with these repository surfaces when deeper detail is required:

- [TRACE method details](method.md)
- [TRACE controls](controls.md)
- [TRACE scoring](scoring.md)
- [TRACE evaluation report template](report-template.md)
- [Stable methodology](../../methodology/README.md)
- [Evaluation contract](../../methodology/evaluation-contract.md)
- [Start here](../start-here.md)
- [Implementation-first path](../implementation-first.md)
- [Operator playbook](../operator-playbook.md)
- [Executable governance](../executable-governance.md)
- [Evaluations](../evaluations.md)

## In one sentence

> **TRACE turns governance propositions into evidence-backed findings, actionable implementation requirements, and re-evaluable closure claims without taking over the authority of the system or institution being assessed.**

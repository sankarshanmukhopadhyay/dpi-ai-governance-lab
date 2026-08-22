---
layout: default
title: Start here
nav_order: 1
has_children: false
---

# Start here

The DPI AI Governance Lab is a workbench for turning publications and deployment propositions into **evidence-backed governance findings, normalized gaps, remediation requirements, and closure tests**.

## Choose your task

### I need to evaluate a paper or publication

Use the TRACE methodology and deterministic review workflow:

1. read `methodology/README.md`;
2. run `dpi-lab review`;
3. validate the review with `dpi-lab validate`;
4. convert material findings into `governance-gaps.yaml`;
5. validate and summarize gaps with `dpi-lab gaps-validate --summary`.

### I operate or implement a DPI/AI system

Start with the [Operator playbook](operator-playbook.md). The goal is to resolve a governance weakness into a concrete capability, remediation asset, implementation change, and evidence requirement.

### I want to understand what TRACE is finding across publications

Start with [Evaluations](evaluations.md) and the [first real-review gap baseline](../baselines/2026-08-22/README.md).

### I need executable governance or assurance testing

Use [Executable governance](executable-governance.md) after the governance gap and remediation requirement have been made explicit. Executable governance is a verification mechanism inside the improvement loop, not a separate end goal.

## The operator improvement loop

```text
publication / deployment proposition
        ↓
TRACE evaluation
        ↓
evidence-backed governance gap
        ↓
required capability
        ↓
standard remediation
        ↓
implementation
        ↓
closure evidence
        ↓
re-evaluation
```

The companion `dpi-ai-governance-artifacts` repository owns reusable remediation assets. The Lab owns evaluation, normalization, comparison, and closure assessment within the stated scope.

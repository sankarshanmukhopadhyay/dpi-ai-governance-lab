# DPI AI Governance Lab

The DPI AI Governance Lab is a structured, repeatable methodology for
transforming AI and DPI policy papers into enforceable governance
artifacts.

This repository is not a narrative archive. It is a lab environment.
Every paper review must produce comparable, machine-checkable outputs
that can be validated, versioned, and improved over time.

------------------------------------------------------------------------

## Purpose

Most AI governance papers are directionally correct but operationally
vague.\
The Lab applies a deterministic review workflow to:

-   Extract architectural primitives
-   Surface institutional risk structures
-   Bind risks to workflow tiers
-   Define accountability and escalation models
-   Translate insights into reusable governance artifacts

The goal is operational clarity, not commentary.

------------------------------------------------------------------------

## Repository Structure

    artifacts/     Reusable governance artifacts (control mappings, tier models, templates)
    reviews/       Per-paper structured reviews
    papers/        Source documents or paper packs
    docs/          Methodology and reference documentation
    data/          Control IDs, taxonomies, shared reference tables
    schemas/       Machine-readable structures
    tools/         Validators and generators

### Conceptual Separation

-   `artifacts/` = normative governance building blocks
-   `reviews/` = instantiations of the methodology applied to specific
    papers
-   `data/` and `schemas/` = shared validation and taxonomy backbone
-   `tools/` = validation and reproducibility layer

------------------------------------------------------------------------

## How to Review Any Paper (Lab Workflow)

A paper review is treated as a build process with fixed inputs and fixed
outputs.

### Step 1 --- Extract Architectural Primitives

Identify rails, actors, control surfaces, interfaces, decision rights.

### Step 2 --- Identify Institutional Risk Surfaces

Surface failure modes, incentive distortions, accountability gaps.

### Step 3 --- Bind Risk to Workflow Tiers

Map risks to operational tiers (who can act, under what constraints).

### Step 4 --- Define Accountability + Escalation

Specify decision rights, auditability mechanisms, and redress pathways.

### Step 5 --- Convert to Governance Artifacts

Translate insights into structured outputs suitable for conformance and
reuse.

Full method reference: `docs/methodology.md`

------------------------------------------------------------------------

## Creating a New Review

1.  Create a directory:

        reviews/<batch-or-year>/<paper-slug>/

2.  Copy the required templates:

    -   `templates/paper-analysis-template.md` → `paper-analysis.md`
    -   `reviews/templates/paper-review-report-template.md` →
        `paper-review-report.md`
    -   `reviews/templates/paper-review-metadata-template.yaml` →
        `paper-review-metadata.yaml`
    -   `reviews/templates/paper-review-scorecard-template.yaml` →
        `paper-review-scorecard.yaml`

3.  Populate all four files using the 5-step methodology.

4.  Run validators (or rely on CI):

    -   `tools/validators/validate_scorecard.py`
    -   `tools/validators/validate_dossier.py`

    Example:

        python3 tools/validators/validate_scorecard.py reviews/<batch>/<paper-slug>/paper-review-scorecard.yaml
        python3 tools/validators/validate_dossier.py  artifacts/<some-dossier>.json

------------------------------------------------------------------------

## Required Outputs (Contract)

Every review MUST produce:

-   `paper-analysis.md`
-   `paper-review-report.md`
-   `paper-review-metadata.yaml`
-   `paper-review-scorecard.yaml`

These files ensure cross-paper comparability and enable structured
scoring.

------------------------------------------------------------------------

## Review Batches and Evolution

The repository may contain both:

-   `reviews/2026/...` (legacy structure)
-   `reviews/<date>-paper-batch/...` (current structure)

Future reviews should follow the batch-first structure for consistency.

------------------------------------------------------------------------

## Validation and CI

The Lab is designed to be verifiable.

Validators in `tools/validators/` enforce:

-   Scorecard integrity
-   Schema conformance
-   Structural completeness

Scorecards use integer scores on a **0..5** scale (inclusive).

CI workflows ensure that new reviews meet the structural contract.

------------------------------------------------------------------------

## Design Philosophy

Governance must be operational.

Narratives persuade.\
Artifacts enforce.

The DPI AI Governance Lab prioritizes enforceable structure over
rhetorical positioning.

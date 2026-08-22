# DPI AI Governance Lab

![CI](https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-lab/actions/workflows/ci.yml/badge.svg)
![Pages](https://img.shields.io/badge/docs-GitHub%20Pages-blue)

The DPI AI Governance Lab is a **governance evaluation and implementation-readiness workbench** for DPI, AI, agentic systems and consequential digital services.

It can begin from either:

- a publication, policy paper or architecture proposition; or
- a service, product, agent, workflow or deployment that somebody intends to build or improve.

The Lab turns those inputs into **evidence-backed findings, normalized governance gaps, required capabilities, testable closure criteria and re-evaluation evidence**.

## Start here

| Your task | Recommended entry point |
| --- | --- |
| I am designing or building a DPI/AI system | [`docs/implementation-first.md`](docs/implementation-first.md) |
| I operate an existing system and need to close a governance weakness | [`docs/operator-playbook.md`](docs/operator-playbook.md) |
| I need to evaluate a paper or publication | [`methodology/README.md`](methodology/README.md) |
| I need to prove that a control works | [`docs/executable-governance.md`](docs/executable-governance.md) |
| I want to see a complete worked example | [`docs/digital-statecraft-dpi-demonstration.md`](docs/digital-statecraft-dpi-demonstration.md) |
| I need the rendered documentation map | [`docs/start-here.md`](docs/start-here.md) |

## The improvement loop

```text
publication / system proposition / deployment
        ↓
TRACE evaluation
        ↓
evidence-backed GAP-*
        ↓
required CAP-*
        ↓
reusable remediation
        ↓
implementation + failure-path tests
        ↓
closure evidence
        ↓
TRACE re-evaluation
```

**TRACE (Trust, Risk, Architecture & Conformance Evaluation)** is the evaluation method used by the Lab.

- TRACE docs: `docs/trace/`
- TRACE version: `TRACE_VERSION`
- Evaluation contract: `methodology/evaluation-contract.md`
- Scoring: `methodology/scoring-rubric.md`, `methodology/scoring-scale.md`
- Evidence discipline: `docs/evidence-and-citation-discipline.md`

## Lab ↔ Artifacts responsibility boundary

The companion [`dpi-ai-governance-artifacts`](https://github.com/sankarshanmukhopadhyay/dpi-ai-governance-artifacts) repository is the reusable remediation layer.

### The Lab owns

- evaluation and evidence extraction;
- review outputs and scorecards;
- governance-gap normalization;
- `GAP-* → CAP-*` remediation requirements;
- comparison and synthesis;
- adversarial verification;
- scoped closure assessment and re-evaluation.

### The Artifacts repository owns

- reusable schemas and governed templates;
- remediation registry entries;
- controlled implementation guidance;
- positive/negative test vectors;
- reusable evidence requirements and conformance materials.

### Adopting organizations retain

- legal and institutional authority;
- policy and procurement authority;
- deployment approval;
- authority to delegate, revoke, admit evidence, decide, correct and remedy.

Repository-local historical files under `artifacts/` are supporting Lab material. They are **not** the normative operational remediation layer and do not override the companion Artifacts repository or an adopting institution's authority.

## If you are building something

Use [`docs/implementation-first.md`](docs/implementation-first.md) to turn a service idea into a governable design.

The minimum path is:

1. write the system proposition;
2. identify affected parties, consequential decisions and effects;
3. identify accountable authorities and delegates;
4. pressure-test authority, evidence, lifecycle, redress and correction;
5. encode material weaknesses in `governance-gaps.yaml`;
6. resolve `required_capability.id` in the Artifacts remediation registry;
7. implement controls at runtime enforcement points;
8. exercise positive and negative paths;
9. preserve closure evidence;
10. return to TRACE for verification.

## If you are reviewing a publication

Install the workbench:

```bash
python -m venv .venv
source .venv/bin/activate
pip install .
dpi-lab --version
```

Run a deterministic local review:

```bash
dpi-lab review --pdf /path/to/paper.pdf --slug my-paper --out reviews/my-batch
dpi-lab validate reviews/my-batch/my-paper --level policy
```

A model-backed engine is optional. The repository keeps prompts/raw outputs where applicable so model-assisted work remains inspectable and replayable.

Material governance findings can then be encoded and validated with:

```bash
dpi-lab gaps-validate path/to/governance-gaps.yaml --summary
```

## What a review should produce

The core review contract includes:

- `paper-analysis.md`
- `paper-review-report.md`
- `paper-review-metadata.yaml`
- `paper-review-scorecard.yaml`

The governance-improvement layer adds `governance-gaps.yaml` where material implementation-distance gaps exist.

## What implementation-ready means here

A proposition is not implementation-ready because its architecture diagram is persuasive. It is ready for governed implementation when:

- consequential decisions/effects are explicit;
- authority and delegation are explicit;
- material gaps have normalized capability requirements;
- controls have identifiable runtime enforcement points;
- revocation, failure, correction and redress paths are defined where relevant;
- negative paths are testable;
- required closure evidence is known before deployment;
- residual risks and limitations remain visible.

## Proof of method

The Digital Statecraft DPI first-wave programme is a worked demonstration, not an archive-expansion target.

It shows:

```text
6 source essays
  → 6 reproducible TRACE reviews
  → 19 material implementation-distance gaps
  → 6 recurring capability classes
  → evidence-derived reusable remediation
  → six-capability implementation fixture
  → 9 scenarios / 8 adversarial
  → scoped closure evidence
```

See [`docs/digital-statecraft-dpi-demonstration.md`](docs/digital-statecraft-dpi-demonstration.md).

## Repository map

```text
dpi_lab/        CLI and implementation code
methodology/    TRACE evaluation contract and scoring method
reviews/        Applied review evidence
schemas/        Machine-readable review/governance contracts
docs/           Adoption, evaluation, architecture and assurance guidance
case-studies/   Worked implementation and governance fixtures
calibration/    Method calibration examples
maturity-model/ Governance capability ladder
tools/          Validators and evidence tooling
artifacts/      Historical/supporting Lab material; not the companion remediation authority
```

## Design principle

Governance should be **observable, enforceable, revocable, correctable and evidentiary**.

Narrative is useful when it explains the system. It is insufficient when a claim needs to survive implementation, failure and independent verification.

## Documentation

- Start here: `docs/start-here.md`
- Documentation index: `docs/INDEX.md`
- Operator playbook: `docs/operator-playbook.md`
- Implementation-first path: `docs/implementation-first.md`
- Executable governance: `docs/executable-governance.md`
- Evidence and citation discipline: `docs/evidence-and-citation-discipline.md`

Additional CLI workflows:

- `dpi-lab bundle <review_dir> --out <path>` — portable review bundle
- `dpi-lab compare <path> --out <path-stem>` — comparative JSON/Markdown output

# Public repository baseline

This record captures controls reviewed under issue #26. It is repository assurance evidence, not external certification.

| Control | State | Evidence | Residual risk |
|---|---|---|---|
| Purpose/maturity/experimental authority boundary | PASS | `README.md`, `PROJECT-STATUS.yaml`, `GOVERNANCE.md`, experiment/docs surfaces | Lab results do not acquire external regulatory or normative authority. |
| Licensing/release provenance | PASS | `LICENSE`, `LICENSE.md`, `CHANGELOG.md`, `CITATION.cff` | Publication remains maintainer judgment. |
| Security reporting/supported versions | PASS | `SECURITY.md` | Hosted private-reporting enablement remains platform evidence. |
| Contribution/community/support | PASS | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md`, issue/PR templates | None identified. |
| Dependency updates | PASS | `.github/dependabot.yml` | Hosted Dependabot enablement remains platform evidence. |
| Default-branch protection | PARTIAL | active `protect-main` observed 2026-09-05: PRs, resolved conversations, linear history, deletion/non-fast-forward protection, no bypass actors | No required status check is present; tracked separately. |
| Experiment/evidence integrity | PASS / bounded | workflows, experiments, evidence/docs/publication surfaces | Workflow green is not a governance or assurance conclusion by itself. |
| Authority boundary | PASS | `GOVERNANCE.md`, repository docs | External regulators, institutions, specifications and deployments retain their decision rights. |

## Completion boundary

Repository-owned baseline gaps are closed by the remediation PR. Required-status enforcement remains a GitHub-hosted residual tracked separately rather than represented as PASS.

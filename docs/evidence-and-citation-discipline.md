
# Evidence and citation discipline

The Lab now includes two optional but first-class review artifacts alongside the core review contract:

- `assumption-log.yaml`
- `claim-verification-log.yaml`

These files are not ceremonial appendices. They force reviewers to separate what the paper states, what the reviewer is inferring, and what remains open.

## Why this matters

A review can look polished while quietly blending together direct claims, extrapolations, and unresolved questions. That is exactly how governance work becomes difficult to contest.

The assumption log records where the review depends on unverified premises. The claim verification log records which load-bearing claims were checked, what evidence type supports them, and whether the claim remains unverified or contested.

## Minimum operating rule

For any review that will travel outside the repo, reviewers should capture at least:

1. the assumptions that materially affect the scorecard,
2. the claims that drive the executive thesis,
3. the evidence type used for each claim,
4. the status of any unresolved or contested point.

## Bundle export

`dpi-lab bundle` includes both logs when present so the review can travel as a portable evidence package rather than only as markdown.

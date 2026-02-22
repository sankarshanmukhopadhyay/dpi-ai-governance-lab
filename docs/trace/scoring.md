# TRACE Scoring

TRACE scoring is designed to be **explainable** and **audit-friendly**.

## Scale

Each control is scored on:

- **0 — Absent**
- **1 — Partial / informal**
- **2 — Defined**
- **3 — Implemented**
- **4 — Verified / audited**

## Confidence

Scores should carry a confidence annotation:

- **Low** — claim inferred; weak evidence
- **Medium** — some evidence; gaps remain
- **High** — strong evidence; independently verifiable

## Aggregation

- Control scores may be aggregated by domain (Trust/Risk/Architecture/Conformance).
- Report should avoid false precision; prefer **ranges** and **confidence** over single numbers.

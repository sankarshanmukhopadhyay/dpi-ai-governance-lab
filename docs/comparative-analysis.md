
# Comparative analysis layer

The Lab now supports a comparative layer for working across multiple reviews rather than treating each paper as an isolated object.

Use:

```bash
dpi-lab compare reviews --out run/comparison
```

This writes:

- `run/comparison.md`
- `run/comparison.json`

The comparison output aggregates scorecards, computes average scores across the core governance dimensions, and produces a portable matrix that can be used in synthesis notes, editorial comparisons, and roadmap setting.

This is deliberately simple. The point is to make cross-paper analysis routine, not heroic.

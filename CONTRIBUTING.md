# Contributing

This repo is meant to be **easy to adopt** and **easy to verify**. Contributions that increase clarity, determinism, and testability are the highest leverage.

## Quick start (dev)

1. Create a virtualenv and install:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e ".[test]"
   ```
2. Run checks locally:
   ```bash
   pytest
   dpi-lab --help
   python tools/check_compatibility.py
   ```

## Pull request checklist

- Keep PRs **small and reviewable** (one intent per PR).
- Update docs **in the same PR** when behavior changes.
- For changes that affect outputs or validation:
  - Add/extend **tests** in `tests/`
  - Add/extend **examples** under `reviews/examples-batch/`
  - Update `CHANGELOG.md` (Unreleased section)

## Style

- Prefer clear, boring code over clever code.
- Avoid introducing non-determinism (timestamps, random seeds) into review outputs unless explicitly versioned and gated.

## Reporting issues

If you file an issue, include:
- OS + Python version
- Exact command you ran
- Expected vs actual output
- Minimal reproduction input (or a sanitized sample)

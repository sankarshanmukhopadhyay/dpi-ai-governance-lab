#!/usr/bin/env python3
"""Scaffold a new review directory with required contract artifacts.

Usage:
  tools/generators/new_review_scaffold.py --slug <slug> --out <batch_dir> [--pdf <paper.pdf>]

This script is intentionally dependency-light. For the full workflow, prefer:
  dpi-lab scaffold ...
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow running from repo root without installation
REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from dpi_lab.core.scaffold import scaffold_review  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--slug", required=True)
    p.add_argument("--out", required=True, help="Batch directory")
    p.add_argument("--pdf")
    a = p.parse_args()

    base = Path(a.out).expanduser().resolve()
    base.mkdir(parents=True, exist_ok=True)
    pdf = Path(a.pdf).expanduser().resolve() if a.pdf else None
    d = scaffold_review(base, a.slug, pdf)
    print(str(d))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

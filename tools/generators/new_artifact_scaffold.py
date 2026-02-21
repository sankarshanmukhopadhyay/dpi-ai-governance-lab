#!/usr/bin/env python3
"""Scaffold a new reusable artifact under ./artifacts.

Usage:
  tools/generators/new_artifact_scaffold.py --name <artifact-name>

Creates:
  artifacts/<artifact-name>/README.md
  artifacts/<artifact-name>/templates/
  artifacts/<artifact-name>/schemas/

This keeps the repo's artifact library consistent and discoverable.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True, help="Artifact folder name (kebab-case recommended)")
    a = p.parse_args()

    repo = Path(__file__).resolve().parents[2]
    art = (repo / "artifacts" / a.name).resolve()
    art.mkdir(parents=True, exist_ok=True)
    (art / "templates").mkdir(exist_ok=True)
    (art / "schemas").mkdir(exist_ok=True)

    readme = art / "README.md"
    if not readme.exists():
        readme.write_text(
            f"# {a.name}\n\n"
            "Describe this artifact: what it standardizes, how it is used in reviews, and how it is validated.\n",
            encoding="utf-8",
        )

    print(str(art))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

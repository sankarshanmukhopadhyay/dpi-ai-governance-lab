#!/usr/bin/env python3
"""Basic markdown linter.

Checks:
- CRLF/CR characters
- trailing whitespace
- tab characters
- file ends with newline

Usage:
  tools/linters/lint_markdown.py <path> [<path> ...]

For the full workflow, prefer:
  dpi-lab lint ...
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from dpi_lab.core.lint import lint_markdown_paths  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    if not argv:
        print("usage: lint_markdown.py <path> [<path> ...]")
        return 2

    paths = [Path(x).expanduser().resolve() for x in argv]
    res = lint_markdown_paths(paths)
    if res.ok:
        print("OK")
        return 0
    print("FAILED")
    for e in res.errors:
        print(f"- {e}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

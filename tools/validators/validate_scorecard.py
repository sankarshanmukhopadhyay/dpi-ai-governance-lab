#!/usr/bin/env python3
"""Validate a paper review scorecard YAML.

The Lab treats paper reviews as build artifacts with a fixed contract.
This validator enforces the minimum scorecard structure and basic value
integrity so that downstream aggregation/analysis stays deterministic.

Usage:
  tools/validators/validate_scorecard.py <scorecard.yaml>
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml

# Allow running as a standalone script without installing as a package.
_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from common import ValidationResult, add_error, add_warning, print_result  # noqa: E402


SCORE_KEYS = [
    "tiering_completeness",
    "accountability_plumbing",
    "data_governance",
    "redress",
    "sovereignty",
]

# Observed in the repo today: scores range 0..5.
SCORE_MIN = 0
SCORE_MAX = 5


def _is_number(x: Any) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def validate_scorecard(data: Any, file_path: str | None = None) -> ValidationResult:
    errors: List[str] = []
    warnings: List[str] = []

    is_template = bool(file_path) and "template" in str(file_path).lower()

    if not isinstance(data, dict):
        add_error(errors, "Scorecard root must be a YAML mapping/object", file_path)
        return ValidationResult(False, errors, warnings)

    # version
    version = data.get("version")
    if version is None:
        add_error(errors, "Missing required field 'version'", file_path)
    else:
        if _is_number(version):
            pass
        elif isinstance(version, str):
            try:
                float(version)
            except Exception:
                add_error(errors, "'version' must be a number (e.g., 0.1)", file_path)
        else:
            add_error(errors, "'version' must be a number (e.g., 0.1)", file_path)

    # paper
    paper = data.get("paper")
    if not isinstance(paper, dict):
        add_error(errors, "Missing or invalid 'paper' (must be an object)", file_path)
    else:
        title = paper.get("title")
        year = paper.get("year")
        if not isinstance(title, str) or not title.strip():
            if is_template:
                add_warning(warnings, "paper.title is empty (template)", file_path)
            else:
                add_error(errors, "paper.title must be a non-empty string", file_path)
        if not isinstance(year, int) or isinstance(year, bool):
            add_error(errors, "paper.year must be an integer", file_path)
        else:
            if year == 0 and is_template:
                add_warning(warnings, "paper.year is 0 (template)", file_path)
            elif year < 1900 or year > 2100:
                add_warning(warnings, f"paper.year looks unusual ({year}); expected 1900..2100", file_path)

    # scores
    scores = data.get("scores")
    if not isinstance(scores, dict):
        add_error(errors, "Missing or invalid 'scores' (must be an object)", file_path)
    else:
        missing = [k for k in SCORE_KEYS if k not in scores]
        extra = [k for k in scores.keys() if k not in SCORE_KEYS]
        if missing:
            add_error(errors, "Missing score fields: " + ", ".join(missing), file_path)
        if extra:
            add_warning(warnings, "Unexpected score fields (ignored by validator): " + ", ".join(extra), file_path)

        for k in SCORE_KEYS:
            if k not in scores:
                continue
            v = scores.get(k)
            if not isinstance(v, int) or isinstance(v, bool):
                add_error(errors, f"scores.{k} must be an integer", file_path)
                continue
            if v < SCORE_MIN or v > SCORE_MAX:
                add_error(errors, f"scores.{k} must be in range {SCORE_MIN}..{SCORE_MAX}", file_path)

    # notes
    notes = data.get("notes")
    if notes is None:
        add_warning(warnings, "Missing optional field 'notes' (recommended)", file_path)
    elif not isinstance(notes, list):
        add_error(errors, "'notes' must be a list of strings", file_path)
    else:
        bad = [i for i, n in enumerate(notes) if not isinstance(n, str) or not n.strip()]
        if bad:
            add_error(errors, f"notes entries must be non-empty strings (bad indexes: {bad})", file_path)

    ok = len(errors) == 0
    return ValidationResult(ok, errors, warnings)


def main(argv: List[str]) -> int:
    if len(argv) < 2:
        print("usage: validate_scorecard.py <scorecard.yaml>")
        return 2

    p = Path(argv[1])
    if not p.exists():
        print(f"File not found: {p}")
        return 2

    try:
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"YAML parse error in {p}: {e}")
        return 1

    result = validate_scorecard(data, str(p))
    print_result(result)
    return result.exit_code()


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

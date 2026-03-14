#!/usr/bin/env python3
"""Validate a simple governance scorecard JSON file.

Expected shape:
{
  "system_id": "...",
  "scores": {
    "governance": 0-5,
    "risk": 0-5,
    "evidence": 0-5,
    "redress": 0-5,
    "monitoring": 0-5
  }
}
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

REQUIRED = ["governance", "risk", "evidence", "redress", "monitoring"]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: governance_scorecard.py <scorecard.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    scores = data.get("scores")
    if not isinstance(scores, dict):
        print("FAILED")
        print("- scores must be an object")
        return 1
    errors = []
    for key in REQUIRED:
        value = scores.get(key)
        if not isinstance(value, int) or not (0 <= value <= 5):
            errors.append(f"scores.{key} must be an integer between 0 and 5")
    if errors:
        print("FAILED")
        for err in errors:
            print(f"- {err}")
        return 1
    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

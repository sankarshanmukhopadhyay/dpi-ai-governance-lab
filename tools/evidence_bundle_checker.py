#!/usr/bin/env python3
"""Check for a minimal evidence bundle layout."""
from __future__ import annotations
import sys
from pathlib import Path

REQUIRED = [
    "governance_policy.md",
    "risk_register.json",
    "model_documentation.json",
    "evaluation_results.json",
    "incident_response_plan.md",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: evidence_bundle_checker.py <bundle-dir>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1])
    missing = [name for name in REQUIRED if not (root / name).exists()]
    if missing:
        print("FAILED")
        for item in missing:
            print(f"- missing: {item}")
        return 1
    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

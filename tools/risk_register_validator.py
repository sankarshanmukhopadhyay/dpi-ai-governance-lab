#!/usr/bin/env python3
"""Lightweight validator for machine-readable risk registers."""
from __future__ import annotations
import json
import sys
from pathlib import Path

REQUIRED = ["risk_id", "risk_description", "affected_population", "likelihood", "impact", "mitigation_control_ids", "review_frequency"]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: risk_register_validator.py <risk-register.json>", file=sys.stderr)
        return 2
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    entries = data.get("risks")
    if not isinstance(entries, list) or not entries:
        print("FAILED")
        print("- risks must be a non-empty array")
        return 1
    errors = []
    seen = set()
    for idx, risk in enumerate(entries):
        for field in REQUIRED:
            if field not in risk:
                errors.append(f"risks[{idx}].{field} is required")
        rid = risk.get("risk_id")
        if rid in seen:
            errors.append(f"duplicate risk_id: {rid}")
        seen.add(rid)
        for fld in ("likelihood", "impact"):
            if fld in risk and risk[fld] not in {"low", "medium", "high", "critical"}:
                errors.append(f"risks[{idx}].{fld} must be low|medium|high|critical")
    if errors:
        print("FAILED")
        for err in errors:
            print(f"- {err}")
        return 1
    print("OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

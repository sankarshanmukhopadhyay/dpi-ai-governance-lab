#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "harms" / "harm-chain.schema.json"
EXAMPLES = [ROOT / "templates" / "harm-chain.example.yaml"] + sorted(
    (ROOT / "case-studies" / "harm-chain-pressure-tests").glob("*.yaml")
)


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors: list[str] = []

    for path in EXAMPLES:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        for error in sorted(validator.iter_errors(data), key=lambda e: list(e.path)):
            location = "/".join(str(part) for part in error.path) or "<root>"
            errors.append(f"{path.relative_to(ROOT)}:{location}: {error.message}")

    if errors:
        print("FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK")
    print(f"Validated harm chains: {len(EXAMPLES)}")
    for path in EXAMPLES:
        print(f"- {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

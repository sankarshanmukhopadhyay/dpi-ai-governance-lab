#!/usr/bin/env python3
"""Fail-fast compatibility contract check.

This is intentionally small and dependency-free so CI can run it early.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8").strip()

def main() -> int:
    contract_p = ROOT / "TRACE_COMPATIBILITY.json"
    if not contract_p.exists():
        raise SystemExit("Missing TRACE_COMPATIBILITY.json")

    contract = json.loads(contract_p.read_text(encoding="utf-8"))

    # TRACE_VERSION must match
    trace_p = ROOT / "TRACE_VERSION"
    if trace_p.exists():
        trace = read_text(trace_p)
        if contract.get("trace_version") != trace:
            raise SystemExit(f"TRACE_VERSION mismatch: TRACE_VERSION={trace} contract.trace_version={contract.get('trace_version')}")

    # Repo-specific version checks (best-effort)
    pyproject = ROOT / "pyproject.toml"
    version_file = ROOT / "VERSION"

    if pyproject.exists():
        m = re.search(r'^version\s*=\s*"([^"]+)"', pyproject.read_text(encoding="utf-8"), flags=re.M)
        if not m:
            raise SystemExit("Could not parse version from pyproject.toml")
        v = m.group(1)
        if contract.get("lab", {}).get("version") != v:
            raise SystemExit(f"Lab version mismatch: pyproject={v} contract.lab.version={contract.get('lab', {}).get('version')}")

    if version_file.exists():
        v = read_text(version_file)
        if contract.get("artifacts", {}).get("version") != v:
            raise SystemExit(f"Artifacts version mismatch: VERSION={v} contract.artifacts.version={contract.get('artifacts', {}).get('version')}")

    # Basic mapping sanity: declared pair must exist in compatibility list
    declared = (contract.get("lab", {}).get("version"), contract.get("artifacts", {}).get("version"))
    if all(declared) and not any((c.get("lab"), c.get("artifacts")) == declared for c in contract.get("compatibility", [])):
        raise SystemExit("Contract invalid: declared lab/artifacts pair not present in compatibility[]")

    print("OK: compatibility contract is internally consistent")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

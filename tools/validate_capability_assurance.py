#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "case-studies" / "public-benefit-assurance-handoff"
SCHEMA = ROOT / "schemas" / "assurance" / "capability-assessment.schema.json"


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def derive(profile: dict, assessment: dict) -> str:
    by_id = {item["requirement_id"]: item for item in assessment["requirement_results"]}
    mandatory = [item["id"] for item in profile["requirements"] if item.get("mandatory")]
    if any(rid not in by_id for rid in mandatory):
        return "indeterminate"
    if any(by_id[rid]["result"] == "fail" for rid in mandatory):
        return "fail"
    if any(by_id[rid]["result"] in {"indeterminate", "not_evaluated"} for rid in mandatory):
        return "indeterminate"

    evidence_classes = {item["class"] for item in assessment["evidence"]}
    if not set(profile["required_evidence"]).issubset(evidence_classes):
        return "indeterminate"

    optional = [item["id"] for item in profile["requirements"] if not item.get("mandatory")]
    if any(by_id.get(rid, {}).get("result") == "fail" for rid in optional):
        return "partial"
    return "pass"


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    snapshot = load(CASE / "profile-snapshot.yaml")
    profiles = {item["profile_id"]: item for item in snapshot["profiles"]}
    errors: list[str] = []

    for path in sorted(CASE.glob("assessment-*.yaml")):
        assessment = load(path)
        for error in validator.iter_errors(assessment):
            errors.append(f"{path.name}: schema: {error.message}")
        profile = profiles.get(assessment["subject"]["profile_id"])
        if not profile:
            errors.append(f"{path.name}: unknown profile")
            continue
        if profile["capability_id"] != assessment["subject"]["capability_id"]:
            errors.append(f"{path.name}: capability/profile mismatch")
        if assessment["artifact_baseline"]["commit"] != snapshot["source"]["commit"]:
            errors.append(f"{path.name}: artifact baseline commit mismatch")
        evidence_ids = {item["id"] for item in assessment["evidence"]}
        for result in assessment["requirement_results"]:
            missing_refs = set(result["evidence"]) - evidence_ids
            if missing_refs:
                errors.append(f"{path.name}: unresolved evidence ids {sorted(missing_refs)}")
        for item in assessment["evidence"]:
            evidence_path = item["ref"].split("#", 1)[0]
            if not (ROOT / evidence_path).exists():
                errors.append(f"{path.name}: missing evidence ref {evidence_path}")
        expected = derive(profile, assessment)
        if assessment["overall"] != expected:
            errors.append(f"{path.name}: overall={assessment['overall']} derived={expected}")

    expected_states = {
        "assessment-pass.yaml": "pass",
        "assessment-missing-evidence.yaml": "indeterminate",
        "assessment-failed-requirement.yaml": "fail",
        "assessment-correction-pass.yaml": "pass",
    }
    for name, state in expected_states.items():
        data = load(CASE / name)
        if data["overall"] != state:
            errors.append(f"{name}: expected fixture state {state}")

    if errors:
        print("FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Capability assurance handoff OK")
    print("PASS, FAIL, and missing-evidence INDETERMINATE paths verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

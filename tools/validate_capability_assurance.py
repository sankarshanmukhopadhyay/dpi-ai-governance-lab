#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
CASES_ROOT = ROOT / "case-studies"
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


def discover_cases() -> list[Path]:
    return sorted(
        path for path in CASES_ROOT.iterdir()
        if path.is_dir()
        and (path / "profile-snapshot.yaml").exists()
        and any(path.glob("assessment-*.yaml"))
    )


def validate_external_source_baseline(case: Path, errors: list[str]) -> None:
    baseline_path = case / "source-baseline.yaml"
    if not baseline_path.exists():
        return

    baseline = load(baseline_path)
    source = baseline.get("source") or {}
    commit = source.get("commit", "")
    if not re.fullmatch(r"[0-9a-f]{40}", str(commit)):
        errors.append(f"{case.name}: external source commit must be an immutable 40-hex SHA")

    artifacts = baseline.get("artifacts") or []
    if not artifacts:
        errors.append(f"{case.name}: external source baseline must identify at least one artifact")
    for artifact in artifacts:
        if not artifact.get("path"):
            errors.append(f"{case.name}: external source artifact path is required")
        if not re.fullmatch(r"[0-9a-f]{40}", str(artifact.get("blob_sha", ""))):
            errors.append(f"{case.name}: external source artifact blob_sha must be 40-hex")

    evidence_map_path = case / "evidence-map.yaml"
    if evidence_map_path.exists():
        evidence_map = load(evidence_map_path)
        if evidence_map.get("mapping_status") != "bounded-pressure-test":
            errors.append(f"{case.name}: external evidence mapping must remain bounded-pressure-test")


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors: list[str] = []
    cases = discover_cases()
    total = 0

    for case in cases:
        snapshot = load(case / "profile-snapshot.yaml")
        profiles = {item["profile_id"]: item for item in snapshot["profiles"]}
        validate_external_source_baseline(case, errors)

        evidence_map_path = case / "evidence-map.yaml"
        if evidence_map_path.exists():
            evidence_map = load(evidence_map_path)
            profile = profiles.get(evidence_map.get("profile_id"))
            if not profile:
                errors.append(f"{case.name}: evidence map references unknown profile")
            else:
                mapped = set((evidence_map.get("requirements") or {}).keys())
                required = {item["id"] for item in profile["requirements"] if item.get("mandatory")}
                if mapped != required:
                    errors.append(
                        f"{case.name}: evidence map requirements {sorted(mapped)} "
                        f"do not exactly cover mandatory requirements {sorted(required)}"
                    )

        for path in sorted(case.glob("assessment-*.yaml")):
            total += 1
            assessment = load(path)
            for error in validator.iter_errors(assessment):
                errors.append(f"{case.name}/{path.name}: schema: {error.message}")

            profile = profiles.get(assessment["subject"]["profile_id"])
            if not profile:
                errors.append(f"{case.name}/{path.name}: unknown profile")
                continue
            if profile["capability_id"] != assessment["subject"]["capability_id"]:
                errors.append(f"{case.name}/{path.name}: capability/profile mismatch")
            if assessment["artifact_baseline"]["commit"] != snapshot["source"]["commit"]:
                errors.append(f"{case.name}/{path.name}: artifact baseline commit mismatch")
            if assessment["artifact_baseline"]["interface_version"] != snapshot["source"]["interface_version"]:
                errors.append(f"{case.name}/{path.name}: artifact interface version mismatch")

            evidence_ids = {item["id"] for item in assessment["evidence"]}
            for result in assessment["requirement_results"]:
                missing_refs = set(result["evidence"]) - evidence_ids
                if missing_refs:
                    errors.append(
                        f"{case.name}/{path.name}: unresolved evidence ids {sorted(missing_refs)}"
                    )
            for item in assessment["evidence"]:
                evidence_path = item["ref"].split("#", 1)[0]
                if not (ROOT / evidence_path).exists():
                    errors.append(f"{case.name}/{path.name}: missing evidence ref {evidence_path}")

            expected = derive(profile, assessment)
            if assessment["overall"] != expected:
                errors.append(
                    f"{case.name}/{path.name}: overall={assessment['overall']} derived={expected}"
                )

    if errors:
        print("FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Capability assurance handoff OK: {total} assessments across {len(cases)} cases")
    print("External source baselines and bounded evidence mappings verified where present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

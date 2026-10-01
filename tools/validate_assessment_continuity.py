#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "case-studies" / "public-benefit-assurance-handoff"
SCHEMA = ROOT / "schemas" / "assurance" / "assessment-continuity.schema.json"
PROFILE_SNAPSHOT = CASE / "continuity-profile-snapshot.yaml"


def load(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def resolve_ref(ref: str) -> Path:
    return ROOT / ref.split("#", 1)[0]


def derive(profile: dict, continuity: dict) -> str:
    superseded = continuity.get("superseded_by_assessment")
    if superseded:
        target = resolve_ref(superseded["ref"])
        if not target.exists():
            return "indeterminate"
        replacement = load(target)
        if replacement.get("assessment_id") != superseded["assessment_id"]:
            return "indeterminate"
        return "superseded"

    rules = {
        item["event_type"]: item["effect"]
        for item in (profile.get("continuity") or {}).get("rules", [])
    }

    effects: list[str] = []
    unknown_or_unproven = False
    for event in continuity["events"]:
        if not event.get("evidence"):
            unknown_or_unproven = True
            continue
        if any(not resolve_ref(ref).exists() for ref in event["evidence"]):
            unknown_or_unproven = True
            continue
        effect = rules.get(event["event_type"])
        if effect is None:
            unknown_or_unproven = True
            continue
        effects.append(effect)

    if "invalidates" in effects:
        return "invalidated"
    if unknown_or_unproven:
        return "indeterminate"
    if "reassessment_required" in effects:
        return "reassessment_required"
    return "valid"


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    snapshot = load(PROFILE_SNAPSHOT)
    profiles = {item["profile_id"]: item for item in snapshot["profiles"]}
    errors: list[str] = []

    paths = sorted(
        path for path in CASE.glob("continuity-*.yaml")
        if path.name != PROFILE_SNAPSHOT.name
    )

    for path in paths:
        continuity = load(path)
        for error in validator.iter_errors(continuity):
            errors.append(f"{path.name}: schema: {error.message}")

        prior_ref = resolve_ref(continuity["prior_assessment"]["ref"])
        if not prior_ref.exists():
            errors.append(f"{path.name}: prior assessment ref does not exist")
            continue
        prior = load(prior_ref)
        if prior.get("assessment_id") != continuity["prior_assessment"]["assessment_id"]:
            errors.append(f"{path.name}: prior assessment id/ref mismatch")

        profile = profiles.get(continuity["profile_baseline"]["profile_id"])
        if not profile:
            errors.append(f"{path.name}: unknown profile")
            continue
        if prior.get("subject", {}).get("profile_id") != profile["profile_id"]:
            errors.append(f"{path.name}: prior assessment/profile mismatch")
        if continuity["profile_baseline"]["commit"] != snapshot["source"]["commit"]:
            errors.append(f"{path.name}: continuity profile commit mismatch")
        if continuity["profile_baseline"]["interface_version"] != snapshot["source"]["interface_version"]:
            errors.append(f"{path.name}: continuity interface version mismatch")
        if parse_time(continuity["evaluated_at"]) < parse_time(prior["evaluated_at"]):
            errors.append(f"{path.name}: continuity evaluation predates prior assessment")

        expected = derive(profile, continuity)
        if continuity["state"] != expected:
            errors.append(f"{path.name}: state={continuity['state']} derived={expected}")

        replacement_ref = continuity.get("superseded_by_assessment")
        if replacement_ref:
            target = resolve_ref(replacement_ref["ref"])
            if target.exists():
                replacement = load(target)
                if replacement.get("assessment_id") != replacement_ref["assessment_id"]:
                    errors.append(f"{path.name}: replacement assessment id/ref mismatch")
                if replacement.get("subject", {}).get("capability_id") != prior.get("subject", {}).get("capability_id"):
                    errors.append(f"{path.name}: replacement capability mismatch")
                if parse_time(replacement["evaluated_at"]) <= parse_time(prior["evaluated_at"]):
                    errors.append(f"{path.name}: replacement assessment must be later than prior assessment")

    expected_states = {
        "continuity-valid.yaml": "valid",
        "continuity-invalidated.yaml": "invalidated",
        "continuity-reassessment.yaml": "reassessment_required",
        "continuity-superseded.yaml": "superseded",
        "continuity-indeterminate.yaml": "indeterminate",
        "continuity-missing-evidence.yaml": "indeterminate",
    }
    for name, expected in expected_states.items():
        actual = load(CASE / name)["state"]
        if actual != expected:
            errors.append(f"{name}: expected fixture state {expected}, found {actual}")

    if errors:
        print("FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Assessment continuity OK: {len(paths)} cases")
    print("States verified: valid, superseded, reassessment_required, invalidated, indeterminate")
    print("Unknown and missing-evidence changes remain INDETERMINATE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

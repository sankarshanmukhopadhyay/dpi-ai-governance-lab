#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
CASES_ROOT = ROOT / "case-studies"
SCHEMA = ROOT / "schemas" / "assurance" / "assessment-continuity.schema.json"
REQUIRED_STATES = {"valid", "superseded", "reassessment_required", "invalidated", "indeterminate"}


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


def discover_cases() -> list[Path]:
    return sorted(
        path for path in CASES_ROOT.iterdir()
        if path.is_dir()
        and any(
            p.name not in {"continuity-profile-snapshot.yaml"}
            for p in path.glob("continuity-*.yaml")
        )
    )


def snapshot_for(case: Path) -> Path | None:
    dedicated = case / "continuity-profile-snapshot.yaml"
    if dedicated.exists():
        return dedicated
    shared = case / "profile-snapshot.yaml"
    if shared.exists():
        return shared
    return None


def main() -> int:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors: list[str] = []
    total = 0
    tested_cases = 0

    for case in discover_cases():
        snapshot_path = snapshot_for(case)
        if snapshot_path is None:
            errors.append(f"{case.name}: continuity fixtures have no profile snapshot")
            continue

        snapshot = load(snapshot_path)
        profiles = {item["profile_id"]: item for item in snapshot["profiles"]}
        paths = sorted(
            path for path in case.glob("continuity-*.yaml")
            if path.name != "continuity-profile-snapshot.yaml"
        )
        observed_states: set[str] = set()

        for path in paths:
            total += 1
            continuity = load(path)
            observed_states.add(continuity.get("state"))
            for error in validator.iter_errors(continuity):
                errors.append(f"{case.name}/{path.name}: schema: {error.message}")

            prior_ref = resolve_ref(continuity["prior_assessment"]["ref"])
            if not prior_ref.exists():
                errors.append(f"{case.name}/{path.name}: prior assessment ref does not exist")
                continue
            prior = load(prior_ref)
            if prior.get("assessment_id") != continuity["prior_assessment"]["assessment_id"]:
                errors.append(f"{case.name}/{path.name}: prior assessment id/ref mismatch")

            profile = profiles.get(continuity["profile_baseline"]["profile_id"])
            if not profile:
                errors.append(f"{case.name}/{path.name}: unknown profile")
                continue
            if prior.get("subject", {}).get("profile_id") != profile["profile_id"]:
                errors.append(f"{case.name}/{path.name}: prior assessment/profile mismatch")
            if continuity["profile_baseline"]["commit"] != snapshot["source"]["commit"]:
                errors.append(f"{case.name}/{path.name}: continuity profile commit mismatch")
            if continuity["profile_baseline"]["interface_version"] != snapshot["source"]["interface_version"]:
                errors.append(f"{case.name}/{path.name}: continuity interface version mismatch")
            if parse_time(continuity["evaluated_at"]) < parse_time(prior["evaluated_at"]):
                errors.append(f"{case.name}/{path.name}: continuity evaluation predates prior assessment")

            expected = derive(profile, continuity)
            if continuity["state"] != expected:
                errors.append(
                    f"{case.name}/{path.name}: state={continuity['state']} derived={expected}"
                )

            replacement_ref = continuity.get("superseded_by_assessment")
            if replacement_ref:
                target = resolve_ref(replacement_ref["ref"])
                if target.exists():
                    replacement = load(target)
                    if replacement.get("assessment_id") != replacement_ref["assessment_id"]:
                        errors.append(f"{case.name}/{path.name}: replacement assessment id/ref mismatch")
                    if replacement.get("subject", {}).get("capability_id") != prior.get("subject", {}).get("capability_id"):
                        errors.append(f"{case.name}/{path.name}: replacement capability mismatch")
                    if parse_time(replacement["evaluated_at"]) <= parse_time(prior["evaluated_at"]):
                        errors.append(f"{case.name}/{path.name}: replacement assessment must be later than prior assessment")

        if REQUIRED_STATES.issubset(observed_states):
            tested_cases += 1
        else:
            errors.append(
                f"{case.name}: continuity pressure suite does not cover all five states; "
                f"observed={sorted(observed_states)}"
            )

    if errors:
        print("FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Assessment continuity OK: {total} cases across {tested_cases} full five-state suites")
    print("One derivation function handled every discovered continuity case")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Executable governance evaluation validation and evidence helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
from importlib import resources
import json
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


REQUIRED_FILES = ("governance-model.yaml", "scenarios.yaml")


@dataclass
class GovernanceValidationResult:
    ok: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def _load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _schema() -> dict[str, Any]:
    text = (
        resources.files("dpi_lab.resources")
        .joinpath("schemas/governance-model.schema.json")
        .read_text(encoding="utf-8")
    )
    return json.loads(text)


def _ids(items: list[dict[str, Any]], label: str, errors: list[str]) -> set[str]:
    values = [item.get("id") for item in items]
    if len(values) != len(set(values)):
        errors.append(f"duplicate {label} id")
    return {value for value in values if isinstance(value, str)}


def validate_governance_dir(path: Path) -> GovernanceValidationResult:
    path = path.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    for name in REQUIRED_FILES:
        if not (path / name).is_file():
            errors.append(f"missing required file: {name}")
    if errors:
        return GovernanceValidationResult(False, errors, warnings)

    model = _load_yaml(path / "governance-model.yaml")
    scenarios = _load_yaml(path / "scenarios.yaml")

    validator = Draft202012Validator(_schema())
    for error in sorted(validator.iter_errors(model), key=lambda e: list(e.path)):
        loc = ".".join(str(p) for p in error.path) or "$"
        errors.append(f"governance-model.yaml:{loc}: {error.message}")

    if not isinstance(scenarios, dict) or not isinstance(scenarios.get("scenarios"), list):
        errors.append("scenarios.yaml must contain a scenarios list")
        return GovernanceValidationResult(False, errors, warnings)

    if errors:
        return GovernanceValidationResult(False, errors, warnings)

    authority_ids = _ids(model["authority"], "authority", errors)
    action_ids = _ids(model["actions"], "action", errors)
    evidence_ids = _ids(model["evidence_requirements"], "evidence requirement", errors)
    delegation_ids = _ids(model.get("delegations", []), "delegation", errors)

    for delegation in model.get("delegations", []):
        if delegation["authority_ref"] not in authority_ids:
            errors.append(
                f"delegation {delegation['id']} references unknown authority {delegation['authority_ref']}"
            )

    for point in model["decision_points"]:
        if point["action_ref"] not in action_ids:
            errors.append(
                f"decision point {point['id']} references unknown action {point['action_ref']}"
            )
        for evidence_ref in point.get("evidence_refs", []):
            if evidence_ref not in evidence_ids:
                errors.append(
                    f"decision point {point['id']} references unknown evidence {evidence_ref}"
                )

    required_vector_types = {"scope", "revocation", "evidence", "redress"}
    observed_vector_types: set[str] = set()
    scenario_ids: set[str] = set()
    for scenario in scenarios["scenarios"]:
        sid = scenario.get("id")
        if not isinstance(sid, str) or not sid:
            errors.append("scenario id must be a non-empty string")
            continue
        if sid in scenario_ids:
            errors.append(f"duplicate scenario id: {sid}")
        scenario_ids.add(sid)
        vector_type = scenario.get("vector_type")
        if isinstance(vector_type, str):
            observed_vector_types.add(vector_type)
        if scenario.get("expected_outcome") not in {
            "allow",
            "deny",
            "fail_closed",
            "assurance_failure",
            "governance_failure",
        }:
            errors.append(f"scenario {sid} has invalid expected_outcome")

    if delegation_ids:
        missing = sorted(required_vector_types - observed_vector_types)
        if missing:
            errors.append(
                "delegated governance evaluations require negative-vector coverage for: "
                + ", ".join(missing)
            )

    if not model.get("redress"):
        errors.append("at least one redress path is required")

    claims = model.get("governance_claims", [])
    if not any(claim.get("claim_authority") == "upstream" for claim in claims):
        warnings.append("no upstream-authority governance claim is declared")

    return GovernanceValidationResult(not errors, errors, warnings)


def write_evidence_manifest(path: Path, out: Path | None = None) -> Path:
    path = path.resolve()
    result = validate_governance_dir(path)
    if not result.ok:
        raise ValueError("cannot generate evidence manifest for invalid evaluation: " + "; ".join(result.errors))

    entries = []
    for name in REQUIRED_FILES:
        target = path / name
        entries.append(
            {
                "path": name,
                "sha256": sha256(target.read_bytes()).hexdigest(),
            }
        )

    manifest = {
        "manifest_version": "1.0",
        "evaluation_id": _load_yaml(path / "governance-model.yaml")["evaluation_id"],
        "artifacts": entries,
    }
    out = out.resolve() if out else path / "evidence-manifest.json"
    out.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return out


def verify_evidence_manifest(path: Path) -> GovernanceValidationResult:
    path = path.resolve()
    manifest_path = path / "evidence-manifest.json"
    if not manifest_path.is_file():
        return GovernanceValidationResult(False, ["missing evidence-manifest.json"], [])

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    for artifact in manifest.get("artifacts", []):
        rel = artifact.get("path")
        expected = artifact.get("sha256")
        if not isinstance(rel, str) or not isinstance(expected, str):
            errors.append("manifest artifact entries require path and sha256")
            continue
        target = path / rel
        if not target.is_file():
            errors.append(f"manifest artifact missing: {rel}")
            continue
        actual = sha256(target.read_bytes()).hexdigest()
        if actual != expected:
            errors.append(f"manifest hash mismatch: {rel}")
    return GovernanceValidationResult(not errors, errors, [])

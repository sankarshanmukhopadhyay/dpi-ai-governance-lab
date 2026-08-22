from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

from dpi_lab.core.schemas import load_schema


@dataclass
class GapValidationResult:
    ok: bool
    errors: list[str]
    warnings: list[str]
    summary: dict[str, Any]


def _load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _schema_errors(instance: Any) -> list[str]:
    schema = load_schema("schemas/findings/governance-gaps.schema.json")
    validator = Draft202012Validator(schema)
    errors: list[str] = []
    for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path)):
        path = "/".join(str(part) for part in error.path)
        errors.append(f"{path}: {error.message}" if path else error.message)
    return errors


def _summary(instance: dict[str, Any]) -> dict[str, Any]:
    gaps = instance.get("gaps", []) or []
    counts = {
        "total": len(gaps),
        "open": 0,
        "remediation_available": 0,
        "implementation_pending": 0,
        "verification_pending": 0,
        "closed": 0,
        "accepted_risk": 0,
        "coverage_none": 0,
        "coverage_partial": 0,
        "coverage_standardized": 0,
    }
    for gap in gaps:
        status = gap.get("status")
        if status in counts:
            counts[status] += 1
        coverage = (gap.get("remediation") or {}).get("coverage")
        key = f"coverage_{coverage}"
        if key in counts:
            counts[key] += 1

    total = counts["total"]
    addressed = counts["coverage_partial"] + counts["coverage_standardized"]
    standardized = counts["coverage_standardized"]
    closed = counts["closed"]
    counts["artifact_coverage_ratio"] = round(addressed / total, 4) if total else 0.0
    counts["standardized_remediation_ratio"] = round(standardized / total, 4) if total else 0.0
    counts["closure_ratio"] = round(closed / total, 4) if total else 0.0
    return counts


def validate_gap_register(path: Path) -> GapValidationResult:
    path = path.resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not path.exists():
        return GapValidationResult(False, [f"Gap register not found: {path}"], [], {})

    try:
        instance = _load_yaml(path)
    except Exception as exc:
        return GapValidationResult(False, [f"Invalid YAML: {exc}"], [], {})

    if not isinstance(instance, dict):
        return GapValidationResult(False, ["Gap register root must be an object"], [], {})

    errors.extend(_schema_errors(instance))
    if errors:
        return GapValidationResult(False, errors, warnings, _summary(instance))

    gap_ids: set[str] = set()
    capability_ids: set[str] = set()
    for index, gap in enumerate(instance.get("gaps", [])):
        gap_id = gap["gap_id"]
        if gap_id in gap_ids:
            errors.append(f"gaps/{index}/gap_id: duplicate gap_id {gap_id}")
        gap_ids.add(gap_id)

        capability_id = gap["required_capability"]["id"]
        capability_ids.add(capability_id)

        remediation = gap["remediation"]
        coverage = remediation["coverage"]
        artifacts = remediation.get("artifacts", []) or []
        status = gap["status"]

        if coverage == "standardized" and not artifacts:
            errors.append(f"{gap_id}: standardized remediation MUST reference at least one artifact")
        if coverage == "none" and artifacts:
            errors.append(f"{gap_id}: coverage 'none' MUST NOT reference remediation artifacts")
        if status == "remediation_available" and coverage == "none":
            errors.append(f"{gap_id}: remediation_available requires partial or standardized remediation coverage")
        if status == "closed" and coverage == "none":
            errors.append(f"{gap_id}: closed gaps require a remediation path")
        if status == "closed" and not gap["closure"]["required_evidence"]:
            errors.append(f"{gap_id}: closed gaps require closure evidence requirements")

        for artifact in artifacts:
            if artifact["repository"] == "sankarshanmukhopadhyay/dpi-ai-governance-artifacts" and artifact.get("normative") is True:
                warnings.append(
                    f"{gap_id}: artifact repository reference marked normative; verify that normativity is explicitly delegated rather than inferred"
                )

    summary = _summary(instance)
    if summary["total"] and summary["coverage_none"] == summary["total"]:
        warnings.append("No identified gap has a remediation path yet")

    return GapValidationResult(ok=not errors, errors=errors, warnings=warnings, summary=summary)


def format_gap_summary(result: GapValidationResult) -> str:
    summary = result.summary
    if not summary:
        return "No gap summary available"
    return "\n".join(
        [
            f"Total gaps: {summary['total']}",
            f"Standardized remediation: {summary['coverage_standardized']}",
            f"Partial remediation: {summary['coverage_partial']}",
            f"No remediation: {summary['coverage_none']}",
            f"Closed: {summary['closed']}",
            f"Artifact coverage ratio: {summary['artifact_coverage_ratio']:.2%}",
            f"Standardized remediation ratio: {summary['standardized_remediation_ratio']:.2%}",
            f"Closure ratio: {summary['closure_ratio']:.2%}",
        ]
    )

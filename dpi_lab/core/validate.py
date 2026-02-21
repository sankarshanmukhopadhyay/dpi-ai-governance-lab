from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import yaml
from jsonschema import Draft202012Validator


@dataclass
class ValidationResult:
    ok: bool
    errors: List[str]
    warnings: List[str]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _load_json(p: Path) -> Any:
    return json.loads(p.read_text(encoding="utf-8"))


def _load_yaml(p: Path) -> Any:
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def _validate_schema(instance: Any, schema: Dict[str, Any], label: str) -> list[str]:
    v = Draft202012Validator(schema)
    out: List[str] = []
    for e in sorted(v.iter_errors(instance), key=lambda x: list(x.path)):
        path = "/".join([str(x) for x in e.path])
        out.append(f"{label}: {path}: {e.message}")
    return out


def validate_review_dir(review_dir: Path) -> ValidationResult:
    """Validate a single review directory.

    The Lab has two layers:
    - *Contract* (MUST): the four review outputs exist and validate.
    - *Deterministic run artifacts* (SHOULD): pdf, extracted text, and manifest.

    This validator enforces the contract as errors, and treats missing
    run artifacts as warnings so legacy reviews don't break.
    """

    review_dir = review_dir.resolve()
    errors: List[str] = []
    warnings: List[str] = []

    # Contract artifacts (MUST)
    contract = [
        "paper-analysis.md",
        "paper-review-report.md",
        "paper-review-metadata.yaml",
        "paper-review-scorecard.yaml",
    ]
    for rel in contract:
        if not (review_dir / rel).exists():
            errors.append(f"Missing required artifact: {rel}")

    # Deterministic run artifacts (SHOULD)
    should_have = [
        "paper.pdf",
        "extracted/paper.text.v1.txt",
        "run/manifest.json",
    ]
    for rel in should_have:
        if not (review_dir / rel).exists():
            warnings.append(f"Missing recommended deterministic run artifact: {rel}")

    repo = _repo_root()
    meta_schema_p = repo / "schemas" / "reviews" / "paper-review-metadata.schema.json"
    score_schema_p = repo / "schemas" / "reviews" / "paper-review-scorecard.schema.json"

    # Schema checks
    meta_p = review_dir / "paper-review-metadata.yaml"
    if meta_schema_p.exists() and meta_p.exists():
        schema = _load_json(meta_schema_p)
        inst = _load_yaml(meta_p)
        errors.extend(_validate_schema(inst, schema, "metadata"))
    else:
        warnings.append("Metadata schema not found or metadata missing; skipping schema validation")

    score_p = review_dir / "paper-review-scorecard.yaml"
    if score_schema_p.exists() and score_p.exists():
        schema = _load_json(score_schema_p)
        inst = _load_yaml(score_p)
        errors.extend(_validate_schema(inst, schema, "scorecard"))
    else:
        warnings.append("Scorecard schema not found or scorecard missing; skipping schema validation")

    # Manifest JSON parses (if present)
    man = review_dir / "run" / "manifest.json"
    if man.exists():
        try:
            _load_json(man)
        except Exception as ex:
            errors.append(f"manifest.json is not valid JSON: {ex}")

    return ValidationResult(ok=(len(errors) == 0), errors=errors, warnings=warnings)

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List

import yaml
from jsonschema import Draft202012Validator

from dpi_lab.core.schemas import load_schema


@dataclass
class ValidationResult:
    ok: bool
    errors: List[str]
    warnings: List[str]



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

    # Load schemas (from packaged resources in pip installs; fallback to repo paths in editable installs)
    meta_schema = load_schema("schemas/reviews/paper-review-metadata.schema.json")
    score_schema = load_schema("schemas/reviews/paper-review-scorecard.schema.json")

    # Schema checks
    meta_p = review_dir / "paper-review-metadata.yaml"
    if meta_p.exists():
        schema = meta_schema
        inst = _load_yaml(meta_p)
        errors.extend(_validate_schema(inst, schema, "metadata"))
    else:
        warnings.append("Metadata missing; skipping schema validation")

    score_p = review_dir / "paper-review-scorecard.yaml"
    if score_p.exists():
        schema = score_schema
        inst = _load_yaml(score_p)
        errors.extend(_validate_schema(inst, schema, "scorecard"))
    else:
        warnings.append("Scorecard missing; skipping schema validation")

    # Manifest JSON parses (if present)
    man = review_dir / "run" / "manifest.json"
    if man.exists():
        try:
            _load_json(man)
        except Exception as ex:
            errors.append(f"manifest.json is not valid JSON: {ex}")

    # Light-weight markdown sanity (SHOULD) to keep legacy reviews compatible.
    analysis_md = review_dir / "paper-analysis.md"
    if analysis_md.exists():
        txt = analysis_md.read_text(encoding="utf-8", errors="replace")
        if "## Executive" not in txt:
            warnings.append("paper-analysis.md missing expected heading '## Executive summary' (recommended)")
    report_md = review_dir / "paper-review-report.md"
    if report_md.exists():
        txt = report_md.read_text(encoding="utf-8", errors="replace")
        if "## Executive thesis" not in txt:
            warnings.append("paper-review-report.md missing expected heading '## Executive thesis' (recommended)")

    return ValidationResult(ok=(len(errors) == 0), errors=errors, warnings=warnings)


def validate_tree(root: Path) -> ValidationResult:
    """Validate a review directory or a tree of review directories.

    If root looks like a single review directory (contains a scorecard or metadata),
    validate it. Otherwise, recursively validate each subdirectory that contains a
    scorecard file, aggregating results.
    """
    root = root.resolve()
    marker_files = ["paper-review-scorecard.yaml", "paper-review-metadata.yaml"]
    if any((root / m).exists() for m in marker_files):
        return validate_review_dir(root)

    errors: List[str] = []
    warnings: List[str] = []
    found = 0
    for p in root.rglob("paper-review-scorecard.yaml"):
        review_dir = p.parent
        found += 1
        res = validate_review_dir(review_dir)
        if not res.ok:
            errors.append(f"{review_dir}: " + "; ".join(res.errors))
        warnings.extend([f"{review_dir}: {w}" for w in res.warnings])

    if found == 0:
        errors.append(f"No review directories found under: {root}")

    return ValidationResult(ok=len(errors) == 0, errors=errors, warnings=warnings)

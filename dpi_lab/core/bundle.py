
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict

import yaml


def _load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_review_bundle(review_dir: Path) -> Dict[str, Any]:
    review_dir = review_dir.resolve()
    manifest = json.loads((review_dir / "run" / "manifest.json").read_text(encoding="utf-8"))
    metadata = _load_yaml(review_dir / "paper-review-metadata.yaml")
    scorecard = _load_yaml(review_dir / "paper-review-scorecard.yaml")
    analysis_md = (review_dir / "paper-analysis.md").read_text(encoding="utf-8")
    report_md = (review_dir / "paper-review-report.md").read_text(encoding="utf-8")
    assumption_log = _load_yaml(review_dir / "assumption-log.yaml") if (review_dir / "assumption-log.yaml").exists() else None
    claim_log = _load_yaml(review_dir / "claim-verification-log.yaml") if (review_dir / "claim-verification-log.yaml").exists() else None

    included_files = {}
    for rel in [
        "paper-review-metadata.yaml",
        "paper-review-scorecard.yaml",
        "paper-analysis.md",
        "paper-review-report.md",
        "run/manifest.json",
        "assumption-log.yaml",
        "claim-verification-log.yaml",
    ]:
        p = review_dir / rel
        if p.exists():
            included_files[rel] = {"sha256": _sha256(p), "bytes": p.stat().st_size}

    return {
        "bundle_type": "dpi-ai-governance-lab.review-bundle",
        "bundle_version": 1,
        "review_dir": str(review_dir),
        "metadata": metadata,
        "scorecard": scorecard,
        "analysis_markdown": analysis_md,
        "report_markdown": report_md,
        "assumption_log": assumption_log,
        "claim_verification_log": claim_log,
        "manifest": manifest,
        "included_files": included_files,
    }


def write_review_bundle(review_dir: Path, out_path: Path) -> Path:
    bundle = build_review_bundle(review_dir)
    out_path = out_path.resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(bundle, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out_path

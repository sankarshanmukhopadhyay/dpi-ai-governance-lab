from __future__ import annotations

import json
from pathlib import Path

import yaml

from dpi_lab.core.extract import extract_pdf
from dpi_lab.core.local_engine import generate_local_review
from dpi_lab.core.scaffold import scaffold_review
from dpi_lab.core.utils import safe_write_text


def run_review(pdf_path: Path, base_dir: Path, slug: str, engine: str = "local") -> Path:
    """End-to-end review pipeline.

    Today this supports a deterministic 'local' engine that:
    - extracts and canonicalizes text
    - scaffolds the review directory
    - populates metadata + scorecard deterministically
    - leaves analysis/report mostly template-based with a deterministic header

    This keeps the repo runnable for any user while preserving a stable
    contract for future model-backed engines.
    """

    review_dir = scaffold_review(base_dir=base_dir, slug=slug, pdf_path=pdf_path)

    # Extract
    extracted_dir = review_dir / "extracted"
    res = extract_pdf(pdf_path=review_dir / "paper.pdf", out_dir=extracted_dir)

    # Engine
    if engine != "local":
        raise ValueError(f"Unsupported engine: {engine}")

    local = generate_local_review(extracted_dir / "paper.text.v1.txt")

    # Populate metadata.yaml
    metadata_path = review_dir / "paper-review-metadata.yaml"
    metadata = {
        "title": local.title,
        "authors": [],
        "published_year": local.year,
        "source": str(pdf_path),
        "tags": ["generated", "deterministic", "local-engine"],
    }
    metadata_path.write_text(yaml.safe_dump(metadata, sort_keys=False), encoding="utf-8")

    # Populate scorecard.yaml (0 scores in local mode)
    scorecard_path = review_dir / "paper-review-scorecard.yaml"
    scorecard = {
        "version": 0.1,
        "paper": {"title": local.title, "year": local.year},
        "scores": {
            "tiering_completeness": 0,
            "accountability_plumbing": 0,
            "data_governance": 0,
            "redress": 0,
            "sovereignty": 0,
        },
        "notes": [
            "Local deterministic engine does not infer evidence-backed scores.",
            "Replace 0s with rubric-justified scores after completing sections 1-9 of the review report.",
        ],
    }
    scorecard_path.write_text(yaml.safe_dump(scorecard, sort_keys=False), encoding="utf-8")

    # Prepend deterministic header to analysis/report if they still match templates
    analysis_path = review_dir / "paper-analysis.md"
    if analysis_path.exists():
        analysis_txt = analysis_path.read_text(encoding="utf-8")
        if "Paper Analysis Template" in analysis_txt[:200]:
            safe_write_text(
                analysis_path,
                f"# Paper Analysis\n\n> Deterministic local-engine scaffold. Fill this using the Lab methodology.\n\n" + analysis_txt,
            )

    report_path = review_dir / "paper-review-report.md"
    if report_path.exists():
        rep = report_path.read_text(encoding="utf-8")
        if "Paper review report (template)" in rep[:200]:
            safe_write_text(
                report_path,
                f"# Paper review report\n\n> Deterministic local-engine scaffold. Thesis and gaps prefilled; complete remaining sections.\n\n"
                f"## Executive thesis\n{local.executive_thesis}\n\n"
                f"## Strengths (initial)\n" + "\n".join([f"- {x}" for x in local.strengths]) + "\n\n"
                f"## Gaps (initial)\n" + "\n".join([f"- {x}" for x in local.gaps]) + "\n\n"
                + rep,
            )

    # Manifest
    manifest_path = review_dir / "run" / "manifest.json"
    manifest = {
        "version": 1,
        "engine": engine,
        "inputs": {
            "pdf": str((review_dir / "paper.pdf").resolve()),
            "pdf_sha256": res["pdf_sha256"],
            "text_sha256": res["text_sha256"],
        },
        "outputs": {
            "review_dir": str(review_dir.resolve()),
            "metadata": str(metadata_path.resolve()),
            "scorecard": str(scorecard_path.resolve()),
            "analysis": str(analysis_path.resolve()),
            "report": str(report_path.resolve()),
        },
    }
    safe_write_text(manifest_path, json.dumps(manifest, indent=2) + "\n")

    return review_dir

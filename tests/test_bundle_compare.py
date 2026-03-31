
from __future__ import annotations

import json
from pathlib import Path

import yaml

from dpi_lab.core.bundle import write_review_bundle
from dpi_lab.core.compare import write_comparison
from dpi_lab.core.scaffold import scaffold_review


def _populate_review(review_dir: Path, title: str, year: int, score_base: int) -> None:
    (review_dir / "paper-analysis.md").write_text("# Paper Analysis\n\n## Executive summary\nA structured summary.\n", encoding="utf-8")
    (review_dir / "paper-review-report.md").write_text("# Report\n\n## Executive thesis\nA structured thesis.\n", encoding="utf-8")
    (review_dir / "paper-review-metadata.yaml").write_text(
        yaml.safe_dump({"title": title, "authors": ["A"], "published_year": year, "source": "local", "tags": ["demo"]}, sort_keys=False),
        encoding="utf-8",
    )
    (review_dir / "paper-review-scorecard.yaml").write_text(
        yaml.safe_dump(
            {
                "version": 1,
                "paper": {"title": title, "year": year},
                "scores": {
                    "tiering_completeness": score_base,
                    "accountability_plumbing": score_base,
                    "data_governance": score_base,
                    "redress": score_base,
                    "sovereignty": score_base,
                },
                "notes": ["demo"],
            },
            sort_keys=False,
        ),
        encoding="utf-8",
    )
    (review_dir / "run").mkdir(exist_ok=True)
    (review_dir / "run" / "manifest.json").write_text(json.dumps({"version": 1, "engine": "local"}), encoding="utf-8")


def test_write_review_bundle(tmp_path: Path) -> None:
    review_dir = scaffold_review(tmp_path, slug="demo")
    _populate_review(review_dir, "Demo Paper", 2026, 3)
    out = tmp_path / "bundle.json"
    write_review_bundle(review_dir, out)
    data = json.loads(out.read_text(encoding="utf-8"))
    assert data["bundle_type"] == "dpi-ai-governance-lab.review-bundle"
    assert data["metadata"]["title"] == "Demo Paper"
    assert "paper-review-scorecard.yaml" in data["included_files"]


def test_write_comparison(tmp_path: Path) -> None:
    r1 = scaffold_review(tmp_path, slug="r1")
    r2 = scaffold_review(tmp_path, slug="r2")
    _populate_review(r1, "Paper One", 2025, 2)
    _populate_review(r2, "Paper Two", 2026, 4)
    outputs = write_comparison(tmp_path, tmp_path / "comparison")
    data = json.loads(outputs["json"].read_text(encoding="utf-8"))
    assert data["review_count"] == 2
    assert data["reviews"][0]["title"] == "Paper Two"
    assert outputs["markdown"].exists()

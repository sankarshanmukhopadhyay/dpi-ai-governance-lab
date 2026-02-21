from __future__ import annotations

import json
from pathlib import Path

import yaml

from dpi_lab.core.engines import get_engine
from dpi_lab.core.extract import extract_pdf
from dpi_lab.core.render import render_analysis_md, render_report_md
from dpi_lab.core.scaffold import scaffold_review
from dpi_lab.core.utils import safe_write_text
from dpi_lab.engines.base import EngineConfig


def run_review(
    pdf_path: Path,
    base_dir: Path,
    slug: str,
    engine: str = "local",
    model: str | None = None,
    max_input_chars: int = 180_000,
    chunk_max_chars: int = 60_000,
    chunk_max_count: int = 12,
) -> Path:
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

    # Engine (local or model-backed)
    paper_text = (extracted_dir / "paper.text.v1.txt").read_text(encoding="utf-8")
    pages = None
    pages_path = extracted_dir / "paper.pages.v1.json"
    if pages_path.exists():
        try:
            pages = json.loads(pages_path.read_text(encoding="utf-8")).get("pages")
        except Exception:
            pages = None
    eng = get_engine(engine)
    seed = int(res["pdf_sha256"][:8], 16)
    cfg = EngineConfig(
        model=model or "gpt-5",
        seed=seed,
        max_input_chars=max_input_chars,
        chunk_max_chars=chunk_max_chars,
        chunk_max_count=chunk_max_count,
    )
    result = eng.generate(text=paper_text, pdf_sha256=res["pdf_sha256"], config=cfg, pages=pages)

    # Populate metadata.yaml
    metadata_path = review_dir / "paper-review-metadata.yaml"
    metadata_path.write_text(yaml.safe_dump(result.metadata, sort_keys=False), encoding="utf-8")

    # Populate scorecard.yaml
    scorecard_path = review_dir / "paper-review-scorecard.yaml"
    scorecard_path.write_text(yaml.safe_dump(result.scorecard, sort_keys=False), encoding="utf-8")

    # Render markdown from structured JSON
    analysis_path = review_dir / "paper-analysis.md"
    safe_write_text(analysis_path, render_analysis_md(result.analysis))

    report_path = review_dir / "paper-review-report.md"
    safe_write_text(report_path, render_report_md(result.report))

    # Persist prompts + raw responses for audit/replay
    run_dir = review_dir / "run"
    prompts_dir = run_dir / "prompts"
    responses_dir = run_dir / "responses"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    responses_dir.mkdir(parents=True, exist_ok=True)

    raw = result.raw
    if isinstance(raw, dict) and "prompts" in raw:
        for k, v in raw.get("prompts", {}).items():
            safe_write_text(prompts_dir / f"{k}.txt", v)
    safe_write_text(responses_dir / "raw.json", json.dumps(raw, indent=2, ensure_ascii=False) + "\n")

    # Manifest
    manifest_path = review_dir / "run" / "manifest.json"
    manifest = {
        "version": 1,
        "engine": engine,
        "model": cfg.model,
        "seed": cfg.seed,
        "chunking": {
            "max_input_chars": cfg.max_input_chars,
            "chunk_max_chars": cfg.chunk_max_chars,
            "chunk_max_count": cfg.chunk_max_count,
        },
        "inputs": {
            "pdf": str((review_dir / "paper.pdf").resolve()),
            "pdf_sha256": res["pdf_sha256"],
            "text_sha256": res["text_sha256"],
            "pages_sha256": res.get("pages_sha256"),
        },
        "outputs": {
            "review_dir": str(review_dir.resolve()),
            "metadata": str(metadata_path.resolve()),
            "scorecard": str(scorecard_path.resolve()),
            "analysis": str(analysis_path.resolve()),
            "report": str(report_path.resolve()),
            "prompts_dir": str(prompts_dir.resolve()),
            "responses_dir": str(responses_dir.resolve()),
        },
    }
    safe_write_text(manifest_path, json.dumps(manifest, indent=2) + "\n")

    return review_dir

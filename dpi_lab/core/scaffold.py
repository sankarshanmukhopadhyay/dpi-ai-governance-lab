from __future__ import annotations

import shutil
from pathlib import Path

from dpi_lab.core.utils import safe_write_text


REQUIRED_FILES = {
    "paper-analysis.md": ("templates/paper-analysis-template.md",),
    "paper-review-report.md": ("reviews/templates/paper-review-report-template.md",),
    "paper-review-metadata.yaml": ("reviews/templates/paper-review-metadata-template.yaml",),
    "paper-review-scorecard.yaml": ("reviews/templates/paper-review-scorecard-template.yaml",),
}


def _repo_root() -> Path:
    # dpi_lab/core/scaffold.py -> repo root
    return Path(__file__).resolve().parents[2]


def scaffold_review(base_dir: Path, slug: str, pdf_path: Path | None = None) -> Path:
    """Create a new review directory in base_dir/slug with contract files."""
    repo = _repo_root()
    review_dir = (base_dir / slug).resolve()
    review_dir.mkdir(parents=True, exist_ok=True)

    # Copy templates
    for out_name, (src_rel,) in REQUIRED_FILES.items():
        src = repo / src_rel
        dst = review_dir / out_name
        if not dst.exists():
            shutil.copyfile(src, dst)

    # Make standard subfolders for deterministic runs
    (review_dir / "extracted").mkdir(exist_ok=True)
    (review_dir / "run" / "prompts").mkdir(parents=True, exist_ok=True)
    (review_dir / "run" / "responses").mkdir(parents=True, exist_ok=True)

    if pdf_path:
        pdf_path = pdf_path.resolve()
        dst_pdf = review_dir / "paper.pdf"
        if not dst_pdf.exists():
            shutil.copyfile(pdf_path, dst_pdf)

    # Write a minimal manifest stub if absent
    manifest = review_dir / "run" / "manifest.json"
    if not manifest.exists():
        safe_write_text(
            manifest,
            "{\n  \"version\": 1,\n  \"engine\": null,\n  \"inputs\": {},\n  \"outputs\": {}\n}\n",
        )

    return review_dir

from __future__ import annotations

from pathlib import Path

from dpi_lab.core.scaffold import scaffold_review, REQUIRED_FILES


def test_scaffold_review_creates_required_files(tmp_path: Path) -> None:
    scaffold_review(tmp_path, slug="demo")
    for rel in REQUIRED_FILES.keys():
        assert (tmp_path / "demo" / rel).exists()

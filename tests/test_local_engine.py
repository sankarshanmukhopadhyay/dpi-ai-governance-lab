from __future__ import annotations

from pathlib import Path

from dpi_lab.core.local_engine import guess_title_and_year, generate_local_review


def test_guess_title_and_year() -> None:
    title, year = guess_title_and_year("My Paper Title\nSomething\n2024\n")
    assert title == "My Paper Title"
    assert year == 2024


def test_generate_local_review_deterministic(tmp_path: Path) -> None:
    p = tmp_path / "paper.txt"
    p.write_text("A title\n2023\nThis is some text.", encoding="utf-8")
    r1 = generate_local_review(p)
    r2 = generate_local_review(p)
    assert r1 == r2
    assert r1.title

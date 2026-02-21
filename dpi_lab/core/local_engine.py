from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


@dataclass
class LocalReview:
    title: str
    year: int
    executive_thesis: str
    strengths: list[str]
    gaps: list[str]


def guess_title_and_year(text: str) -> tuple[str, int]:
    # Very conservative heuristics: first non-empty line for title,
    # first 4-digit year seen near the beginning.
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    title = lines[0][:200] if lines else "Untitled Paper"

    head = "\n".join(lines[:50])
    m = re.search(r"\b(19\d{2}|20\d{2})\b", head)
    year = int(m.group(1)) if m else 0
    return title, year


def generate_local_review(extracted_text_path: Path) -> LocalReview:
    text = extracted_text_path.read_text(encoding="utf-8")
    title, year = guess_title_and_year(text)

    # Deterministic baseline statements. No model calls.
    thesis = (
        "This review was generated using the Lab's deterministic local engine. "
        "It provides a structurally correct scaffold and flags where human judgement "
        "or a model-backed engine should be applied to complete the methodology."
    )

    strengths = [
        "Establishes a candidate problem framing (requires human verification).",
        "Provides sufficient text volume for extracting architectural primitives.",
    ]
    gaps = [
        "No automated semantic analysis is performed in local mode; complete sections manually or via a model engine.",
        "Scores are set to 0 by default to avoid implying evidence-backed judgement.",
    ]

    return LocalReview(title=title, year=year, executive_thesis=thesis, strengths=strengths, gaps=gaps)

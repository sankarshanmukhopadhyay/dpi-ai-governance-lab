from __future__ import annotations

from importlib import resources
from typing import Union


def read_text(rel_path: str, encoding: str = "utf-8") -> str:
    """Read text from packaged resources under dpi_lab/resources.

    rel_path is relative to dpi_lab/resources, e.g.:
      - "templates/paper-analysis-template.md"
      - "reviews/templates/paper-review-report-template.md"
      - "schemas/reviews/paper-review-scorecard.schema.json"
    """
    base = resources.files("dpi_lab").joinpath("resources")
    p = base.joinpath(rel_path)
    return p.read_text(encoding=encoding)


def read_bytes(rel_path: str) -> bytes:
    """Read bytes from packaged resources under dpi_lab/resources."""
    base = resources.files("dpi_lab").joinpath("resources")
    p = base.joinpath(rel_path)
    return p.read_bytes()

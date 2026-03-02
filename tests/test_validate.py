from __future__ import annotations

import json
from pathlib import Path

import pytest

from dpi_lab.core.validate import validate_review_dir, validate_tree
from dpi_lab.core.scaffold import scaffold_review


def _write(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")


def test_validate_contract_missing_required_artifacts(tmp_path: Path) -> None:
    res = validate_review_dir(tmp_path, level="contract")
    assert res.ok is False
    assert any("Missing required artifact" in e for e in res.errors)


def test_validate_schema_catches_invalid_yaml(tmp_path: Path) -> None:
    # create required contract files
    _write(tmp_path / "paper-analysis.md", "# analysis\n")
    _write(tmp_path / "paper-review-report.md", "# report\n")
    # invalid metadata: missing required 'title' etc
    _write(tmp_path / "paper-review-metadata.yaml", "authors: []\npublished_year: 2026\nsource: {}\ntags: []\n")
    # minimal scorecard missing required fields too
    _write(tmp_path / "paper-review-scorecard.yaml", "version: 1\n")

    res = validate_review_dir(tmp_path, level="schema")
    assert res.ok is False
    # should contain jsonschema errors
    assert any("metadata:" in e for e in res.errors) or any("scorecard:" in e for e in res.errors)


def test_validate_tree_finds_nested_review_dirs(tmp_path: Path) -> None:
    a = tmp_path / "a"
    a.mkdir()
    scaffold_review(a, slug="t1")
    res = validate_tree(tmp_path, level="contract")
    assert res.ok is True


def test_unknown_validation_level_fails(tmp_path: Path) -> None:
    scaffold_review(tmp_path, slug="x")
    res = validate_review_dir(tmp_path, level="nonsense")
    assert res.ok is False
    assert any("Unknown validation level" in e for e in res.errors)

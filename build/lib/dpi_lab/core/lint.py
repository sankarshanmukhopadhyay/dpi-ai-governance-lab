from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List


@dataclass
class LintResult:
    ok: bool
    errors: List[str]
    warnings: List[str]


def _iter_md_files(paths: Iterable[Path]) -> List[Path]:
    out: List[Path] = []
    for p in paths:
        if p.is_dir():
            out.extend(sorted(p.rglob("*.md")))
        elif p.is_file() and p.suffix.lower() == ".md":
            out.append(p)
    return out


def lint_markdown_paths(paths: Iterable[Path]) -> LintResult:
    errors: List[str] = []
    warnings: List[str] = []

    files = _iter_md_files(paths)
    if not files:
        warnings.append("No markdown files found")
        return LintResult(ok=True, errors=[], warnings=warnings)

    for f in files:
        txt = f.read_text(encoding="utf-8", errors="replace")
        if "\r" in txt:
            errors.append(f"{f}: contains CR characters (use LF newlines)")
        lines = txt.splitlines()
        for i, ln in enumerate(lines, start=1):
            if "\t" in ln:
                errors.append(f"{f}:{i}: contains tab character")
            if ln.rstrip() != ln:
                errors.append(f"{f}:{i}: trailing whitespace")
        if not txt.endswith("\n"):
            errors.append(f"{f}: file must end with a newline")

    return LintResult(ok=(len(errors) == 0), errors=errors, warnings=warnings)

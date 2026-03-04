#!/usr/bin/env python3
"""Minimal documentation audit (internal links + freshness signals).

Design goals:
- Zero external dependencies
- Fast enough for CI
- Focus on Tier-0 docs and internal link integrity
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote

REPO_ROOT = Path(__file__).resolve().parents[1]

MD_EXT = {".md", ".markdown"}

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
BARE_URL_RE = re.compile(r"(https?://[^\s)>\]]+)")
TODO_RE = re.compile(r"\b(TODO|TBD|FIXME)\b")

TIER0 = [
    REPO_ROOT / "README.md",
    REPO_ROOT / "docs" / "overview.md",
    REPO_ROOT / "docs" / "documentation-freshness.md",
]

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

def read_text(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")

def extract_links(text: str) -> list[str]:
    links = []
    for m in LINK_RE.finditer(text):
        links.append(m.group(1).strip())
    for m in IMG_RE.finditer(text):
        links.append(m.group(1).strip())
    for m in BARE_URL_RE.finditer(text):
        links.append(m.group(1).strip().rstrip(".,;:"))
    return links

def normalize_target(target: str) -> str:
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]
    # Handle markdown link title: path "title"
    if " " in target and not target.startswith("http"):
        target = target.split()[0]
    return target

def internal_exists(md_path: Path, target: str) -> tuple[bool, Path | None]:
    if target.startswith(("http://", "https://", "mailto:", "tel:")):
        return True, None
    if target.startswith("#"):
        return True, None

    path_part = target.split("#")[0]
    if not path_part:
        return True, None

    # Absolute-from-repo paths
    if path_part.startswith("/"):
        cand = (REPO_ROOT / path_part.lstrip("/")).resolve()
    else:
        cand = (md_path.parent / unquote(path_part)).resolve()

    # Prevent escaping repo root
    try:
        cand.relative_to(REPO_ROOT)
    except ValueError:
        return False, cand

    return cand.exists(), cand

def md_files() -> list[Path]:
    out = []
    for p in REPO_ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in MD_EXT:
            out.append(p)
    return out

def require_frontmatter_keys(p: Path, keys: list[str]) -> list[str]:
    if not p.exists():
        return [f"missing Tier-0 doc: {p.relative_to(REPO_ROOT)}"]
    m = FRONTMATTER_RE.match(read_text(p))
    if not m:
        return [f"missing frontmatter block: {p.relative_to(REPO_ROOT)}"]
    fm = m.group(1)
    missing = []
    for k in keys:
        if re.search(rf"^\s*{re.escape(k)}\s*:", fm, flags=re.MULTILINE) is None:
            missing.append(f"missing frontmatter key '{k}': {p.relative_to(REPO_ROOT)}")
    return missing

def main() -> int:
    errors: list[str] = []

    # 1) No OS trash
    for p in REPO_ROOT.rglob(".DS_Store"):
        errors.append(f"OS artifact present: {p.relative_to(REPO_ROOT)}")

    # 2) Tier-0 must declare freshness metadata
    for p in [REPO_ROOT / "docs" / "overview.md", REPO_ROOT / "docs" / "documentation-freshness.md"]:
        errors.extend(require_frontmatter_keys(p, ["last_reviewed", "applies_to"]))

    # 3) Tier-0 must not contain TODO/TBD/FIXME
    for p in TIER0:
        if p.exists() and TODO_RE.search(read_text(p)):
            errors.append(f"TODO/TBD/FIXME present in Tier-0 doc: {p.relative_to(REPO_ROOT)}")

    # 4) Internal link integrity across all Markdown
    for p in md_files():
        txt = read_text(p)
        for raw in extract_links(txt):
            t = normalize_target(raw)
            ok, cand = internal_exists(p, t)
            if not ok:
                errors.append(f"broken internal link in {p.relative_to(REPO_ROOT)} -> {t} (resolved: {cand})")

    if errors:
        print("Documentation audit FAILED:\n")
        for e in errors:
            print(f"- {e}")
        return 1

    print("Documentation audit PASSED.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

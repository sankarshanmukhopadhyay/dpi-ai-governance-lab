from __future__ import annotations

"""Deterministic chunking utilities for long papers.

We chunk based on the canonical per-page structure produced by extract.py.

Design goals:
- Deterministic: same extracted pages => same chunks.
- Stable boundaries: chunks are contiguous page ranges.
- Budget-aware: aim to keep each chunk under a character budget.
"""

import hashlib
from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    start_page: int
    end_page: int
    text: str
    sha256: str


def _sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def make_chunks(
    *,
    pages: List[Dict[str, Any]],
    max_chars: int,
    max_count: int,
) -> List[Chunk]:
    """Group pages into contiguous chunks under max_chars.

    - Pages are expected to be in the format: {"page": int, "text": str}
    - Chunk text is the concatenation of page texts with stable separators.
    """

    if max_chars <= 0:
        raise ValueError("max_chars must be > 0")
    if max_count <= 0:
        raise ValueError("max_count must be > 0")

    chunks: List[Chunk] = []
    buf: List[str] = []
    start_page = None

    def flush(end_page: int) -> None:
        nonlocal buf, start_page
        if start_page is None or not buf:
            return
        text = "\n\n".join(buf).strip() + "\n"
        sha = _sha256_text(text)
        cid = f"p{start_page:04d}-p{end_page:04d}-{sha[:8]}"
        chunks.append(Chunk(chunk_id=cid, start_page=start_page, end_page=end_page, text=text, sha256=sha))
        buf = []
        start_page = None

    current_len = 0
    last_page = None
    for p in pages:
        pg = int(p.get("page"))
        txt = str(p.get("text", ""))
        # Stable per-page separator improves readability and reduces accidental merges.
        page_block = f"--- PAGE {pg} ---\n{txt.strip()}\n"
        if start_page is None:
            start_page = pg
            current_len = 0

        # If adding this page exceeds budget, flush current chunk first.
        if buf and (current_len + len(page_block) > max_chars):
            flush(last_page if last_page is not None else pg)
            if len(chunks) >= max_count:
                break
            start_page = pg
            current_len = 0

        buf.append(page_block)
        current_len += len(page_block)
        last_page = pg

    if len(chunks) < max_count and buf and last_page is not None:
        flush(last_page)

    return chunks

from __future__ import annotations

import pytest

from dpi_lab.core.chunking import make_chunks


def test_make_chunks_respects_char_budget_and_contiguity() -> None:
    pages = [{"page": 1, "text": "a" * 50}, {"page": 2, "text": "b" * 50}, {"page": 3, "text": "c" * 50}]
    chunks = make_chunks(pages=pages, max_chars=140, max_count=10)
    # should split at least once (each page block includes separator overhead)
    assert len(chunks) >= 2
    # contiguity and order
    assert chunks[0].start_page == 1
    assert chunks[-1].end_page == 3
    for c in chunks:
        assert c.start_page <= c.end_page
        assert c.text.endswith("\n")


def test_make_chunks_deterministic_ids() -> None:
    pages = [{"page": 1, "text": "hello"}, {"page": 2, "text": "world"}]
    c1 = make_chunks(pages=pages, max_chars=10_000, max_count=10)
    c2 = make_chunks(pages=pages, max_chars=10_000, max_count=10)
    assert [x.chunk_id for x in c1] == [x.chunk_id for x in c2]
    assert [x.sha256 for x in c1] == [x.sha256 for x in c2]


def test_make_chunks_token_budget_requires_counter() -> None:
    pages = [{"page": 1, "text": "hello"}]
    with pytest.raises(ValueError):
        make_chunks(pages=pages, max_chars=10_000, max_count=10, max_tokens=10)

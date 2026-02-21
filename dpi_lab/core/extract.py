from __future__ import annotations

import re
import json
from pathlib import Path

from pypdf import PdfReader

from dpi_lab.core.utils import sha256_file, sha256_bytes, safe_write_text


PAGE_MARKER_FMT = "\n\n--- PAGE {n} ---\n\n"


def canonicalize_text(s: str) -> str:
    # Normalize line endings, strip trailing spaces, collapse excessive blank lines.
    s = s.replace('\r\n', '\n').replace('\r', '\n')
    s = "\n".join([ln.rstrip() for ln in s.split('\n')])
    # Collapse 3+ newlines to 2 newlines
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip() + "\n"


def extract_pdf(pdf_path: Path, out_dir: Path) -> dict:
    """Extract text per page from PDF and write canonicalized outputs.

    Outputs:
      - paper.pdf.sha256
      - paper.text.v1.txt (canonicalized, page-delimited)
      - paper.text.v1.sha256
      - paper.pages.v1.json (canonical per-page text)
      - paper.pages.v1.sha256
    """
    pdf_path = pdf_path.resolve()
    out_dir = out_dir.resolve()

    reader = PdfReader(str(pdf_path))
    pages_text = []
    for i, page in enumerate(reader.pages, start=1):
        try:
            t = page.extract_text() or ""
        except Exception:
            t = ""
        pages_text.append(PAGE_MARKER_FMT.format(n=i) + t)

    combined = "".join(pages_text)
    canon = canonicalize_text(combined)

    # Build a canonical per-page structure for deterministic downstream chunking.
    pages = []
    for i, raw in enumerate(reader.pages, start=1):
        # We re-extract in the loop above; reuse pages_text by stripping the marker.
        # pages_text[i-1] begins with PAGE_MARKER_FMT and then the page text.
        page_block = pages_text[i - 1]
        page_txt = page_block.split(PAGE_MARKER_FMT.format(n=i), 1)[-1]
        page_txt = canonicalize_text(page_txt)
        pages.append({"page": i, "text": page_txt})

    pdf_hash = sha256_file(pdf_path)
    text_hash = sha256_bytes(canon.encode('utf-8'))

    pages_json = json.dumps({"version": 1, "pages": pages}, ensure_ascii=False, indent=2) + "\n"
    pages_hash = sha256_bytes(pages_json.encode("utf-8"))

    safe_write_text(out_dir / "paper.pdf.sha256", pdf_hash + "\n")
    safe_write_text(out_dir / "paper.text.v1.txt", canon)
    safe_write_text(out_dir / "paper.text.v1.sha256", text_hash + "\n")
    safe_write_text(out_dir / "paper.pages.v1.json", pages_json)
    safe_write_text(out_dir / "paper.pages.v1.sha256", pages_hash + "\n")

    return {
        "pdf": str(pdf_path),
        "out": str(out_dir),
        "pdf_sha256": pdf_hash,
        "text_sha256": text_hash,
        "pages_sha256": pages_hash,
        "message": f"Extracted {len(reader.pages)} pages -> {out_dir / 'paper.text.v1.txt'}",
    }

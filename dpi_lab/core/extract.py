from __future__ import annotations

import re
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

    pdf_hash = sha256_file(pdf_path)
    text_hash = sha256_bytes(canon.encode('utf-8'))

    safe_write_text(out_dir / "paper.pdf.sha256", pdf_hash + "\n")
    safe_write_text(out_dir / "paper.text.v1.txt", canon)
    safe_write_text(out_dir / "paper.text.v1.sha256", text_hash + "\n")

    return {
        "pdf": str(pdf_path),
        "out": str(out_dir),
        "pdf_sha256": pdf_hash,
        "text_sha256": text_hash,
        "message": f"Extracted {len(reader.pages)} pages -> {out_dir / 'paper.text.v1.txt'}",
    }

#!/usr/bin/env python3
"""CLI entrypoint for DPI AI Governance Lab workbench.

Goal: make the repo usable as a local workbench:
- extract: PDF -> canonicalized text + hashes
- scaffold: create a review directory with the contract files
- review: extract + generate a deterministic baseline review (local engine)
- validate: enforce the review contract and schemas
- lint: basic markdown hygiene checks

This includes:
- a *local* deterministic engine to keep the workflow runnable without external services
- an optional model-backed engine (OpenAI) that generates JSON-first outputs and renders
  deterministic markdown/yaml artifacts from schema-valid JSON.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from dpi_lab.core.extract import extract_pdf
from dpi_lab.core.review import run_review
from dpi_lab.core.scaffold import scaffold_review
from dpi_lab.core.validate import validate_review_dir
from dpi_lab.core.lint import lint_markdown_paths


def _p(s: str) -> Path:
    return Path(s).expanduser().resolve()


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="dpi-lab", description="DPI AI Governance Lab workbench")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_extract = sub.add_parser("extract", help="Extract and canonicalize text from a PDF")
    p_extract.add_argument("--pdf", required=True, help="Path to PDF")
    p_extract.add_argument("--out", required=True, help="Output directory")

    p_scaffold = sub.add_parser("scaffold", help="Create a new review directory scaffold")
    p_scaffold.add_argument("--slug", required=True, help="Review slug")
    p_scaffold.add_argument("--out", required=True, help="Base output directory (batch folder)")
    p_scaffold.add_argument("--pdf", help="Optional PDF to copy into review dir")

    p_review = sub.add_parser("review", help="Run end-to-end review pipeline")
    p_review.add_argument("--pdf", required=True, help="Path to PDF")
    p_review.add_argument("--slug", required=True, help="Review slug")
    p_review.add_argument("--out", required=True, help="Base output directory (batch folder)")
    p_review.add_argument(
        "--engine",
        default="local",
        choices=["local", "openai"],
        help="Generation engine. 'local' is scaffold-only; 'openai' uses the OpenAI API (requires OPENAI_API_KEY).",
    )
    p_review.add_argument(
        "--model",
        default=None,
        help="Model name for model-backed engines (e.g., gpt-5). Ignored by local engine.",
    )

    p_validate = sub.add_parser("validate", help="Validate a review directory")
    p_validate.add_argument("review_dir", help="Path to a single review directory")

    p_lint = sub.add_parser("lint", help="Lint markdown files for basic hygiene")
    p_lint.add_argument("paths", nargs="+", help="Files or directories")

    return p


def main(argv: list[str] | None = None) -> int:
    argv = argv or sys.argv[1:]
    args = build_parser().parse_args(argv)

    if args.cmd == "extract":
        out = _p(args.out)
        out.mkdir(parents=True, exist_ok=True)
        res = extract_pdf(pdf_path=_p(args.pdf), out_dir=out)
        print(res["message"])
        return 0

    if args.cmd == "scaffold":
        base = _p(args.out)
        base.mkdir(parents=True, exist_ok=True)
        review_dir = scaffold_review(base_dir=base, slug=args.slug, pdf_path=_p(args.pdf) if args.pdf else None)
        print(str(review_dir))
        return 0

    if args.cmd == "review":
        base = _p(args.out)
        base.mkdir(parents=True, exist_ok=True)
        review_dir = run_review(
            pdf_path=_p(args.pdf),
            base_dir=base,
            slug=args.slug,
            engine=args.engine,
            model=args.model,
        )
        print(str(review_dir))
        return 0

    if args.cmd == "validate":
        result = validate_review_dir(_p(args.review_dir))
        if result.ok:
            print("OK")
            if result.warnings:
                print("Warnings:")
                for w in result.warnings:
                    print(f"- {w}")
            return 0

        print("FAILED")
        for e in result.errors:
            print(f"- {e}")
        if result.warnings:
            print("Warnings:")
            for w in result.warnings:
                print(f"- {w}")
        return 1

    if args.cmd == "lint":
        paths = [_p(x) for x in args.paths]
        res = lint_markdown_paths(paths)
        if res.ok:
            print("OK")
            if res.warnings:
                print("Warnings:")
                for w in res.warnings:
                    print(f"- {w}")
            return 0
        print("FAILED")
        for e in res.errors:
            print(f"- {e}")
        return 1

    return 2

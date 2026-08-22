#!/usr/bin/env python3
"""CLI entrypoint for DPI AI Governance Lab workbench."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from dpi_lab import __version__
from dpi_lab.core.extract import extract_pdf
from dpi_lab.core.review import run_review
from dpi_lab.core.scaffold import scaffold_review
from dpi_lab.core.validate import validate_tree
from dpi_lab.core.lint import lint_markdown_paths
from dpi_lab.core.bundle import write_review_bundle
from dpi_lab.core.compare import write_comparison
from dpi_lab.core.findings import format_gap_summary, validate_gap_register
from dpi_lab.core.governance import (
    validate_governance_dir,
    verify_evidence_manifest,
    write_evidence_manifest,
)


def _p(s: str) -> Path:
    return Path(s).expanduser().resolve()


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="dpi-lab", description="DPI AI Governance Lab workbench")
    p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
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
    p_review.add_argument("--engine", default="local", choices=["local", "openai"])
    p_review.add_argument("--model", default=None)
    p_review.add_argument("--max-input-chars", type=int, default=180_000)
    p_review.add_argument("--max-input-tokens", type=int, default=None)
    p_review.add_argument("--chunk-max-chars", type=int, default=60_000)
    p_review.add_argument("--chunk-max-tokens", type=int, default=None)
    p_review.add_argument("--chunk-max-count", type=int, default=12)

    p_validate = sub.add_parser("validate", help="Validate a review directory")
    p_validate.add_argument("path")
    p_validate.add_argument("--level", default="schema", choices=["contract", "schema", "policy", "semantic"])
    p_validate.add_argument("--engine", default=None, choices=["local", "openai"])
    p_validate.add_argument("--model", default=None)
    p_validate.add_argument("--max-input-chars", type=int, default=180_000)
    p_validate.add_argument("--max-input-tokens", type=int, default=None)

    p_lint = sub.add_parser("lint", help="Lint markdown files for basic hygiene")
    p_lint.add_argument("paths", nargs="+")

    p_bundle = sub.add_parser("bundle", help="Export a portable JSON bundle for one review directory")
    p_bundle.add_argument("review_dir")
    p_bundle.add_argument("--out", required=True)

    p_compare = sub.add_parser("compare", help="Build a comparative matrix across review directories")
    p_compare.add_argument("path")
    p_compare.add_argument("--out", required=True)

    p_gap_validate = sub.add_parser(
        "gaps-validate",
        help="Validate a TRACE governance-gap register and report remediation coverage",
    )
    p_gap_validate.add_argument("path")
    p_gap_validate.add_argument(
        "--summary",
        action="store_true",
        help="Print operator-facing remediation and closure metrics",
    )

    p_gov_validate = sub.add_parser(
        "governance-validate",
        help="Validate a TRACE executable-governance evaluation directory",
    )
    p_gov_validate.add_argument("path")
    p_gov_validate.add_argument(
        "--verify-manifest",
        action="store_true",
        help="Also verify evidence-manifest.json hashes",
    )

    p_gov_manifest = sub.add_parser(
        "governance-manifest",
        help="Generate a SHA-256 evidence manifest for a valid governance evaluation",
    )
    p_gov_manifest.add_argument("path")
    p_gov_manifest.add_argument("--out", default=None)

    return p


def _print_result(result) -> int:
    if result.ok:
        print("OK")
        for warning in result.warnings:
            print(f"Warning: {warning}")
        return 0
    print("FAILED")
    for error in result.errors:
        print(f"- {error}")
    for warning in result.warnings:
        print(f"Warning: {warning}")
    return 1


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
            max_input_chars=args.max_input_chars,
            chunk_max_chars=args.chunk_max_chars,
            chunk_max_count=args.chunk_max_count,
            max_input_tokens=args.max_input_tokens,
            chunk_max_tokens=args.chunk_max_tokens,
        )
        print(str(review_dir))
        return 0

    if args.cmd == "validate":
        return _print_result(
            validate_tree(
                _p(args.path),
                level=args.level,
                semantic_engine=args.engine,
                model=args.model,
                max_input_chars=args.max_input_chars,
                max_input_tokens=args.max_input_tokens,
            )
        )

    if args.cmd == "lint":
        return _print_result(lint_markdown_paths([_p(x) for x in args.paths]))

    if args.cmd == "bundle":
        print(str(write_review_bundle(_p(args.review_dir), _p(args.out))))
        return 0

    if args.cmd == "compare":
        outputs = write_comparison(_p(args.path), _p(args.out))
        print(str(outputs["markdown"]))
        print(str(outputs["json"]))
        return 0

    if args.cmd == "gaps-validate":
        result = validate_gap_register(_p(args.path))
        exit_code = _print_result(result)
        if args.summary:
            print(format_gap_summary(result))
        return exit_code

    if args.cmd == "governance-validate":
        result = validate_governance_dir(_p(args.path))
        if result.ok and args.verify_manifest:
            result = verify_evidence_manifest(_p(args.path))
        return _print_result(result)

    if args.cmd == "governance-manifest":
        try:
            out = write_evidence_manifest(
                _p(args.path),
                _p(args.out) if args.out else None,
            )
        except ValueError as exc:
            print(f"FAILED\n- {exc}")
            return 1
        print(str(out))
        return 0

    return 2

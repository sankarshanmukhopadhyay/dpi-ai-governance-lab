from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict

from dpi_lab.engines.base import EngineConfig, EngineResult, ReviewEngine


@dataclass
class LocalReview:
    title: str
    year: int
    executive_thesis: str
    strengths: list[str]
    gaps: list[str]


def guess_title_and_year(text: str) -> tuple[str, int]:
    # Very conservative heuristics: first non-empty line for title,
    # first 4-digit year seen near the beginning.
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    title = lines[0][:200] if lines else "Untitled Paper"

    head = "\n".join(lines[:50])
    m = re.search(r"\b(19\d{2}|20\d{2})\b", head)
    year = int(m.group(1)) if m else 0
    return title, year


def generate_local_review(extracted_text_path: Path) -> LocalReview:
    text = extracted_text_path.read_text(encoding="utf-8")
    title, year = guess_title_and_year(text)

    # Deterministic baseline statements. No model calls.
    thesis = (
        "This review was generated using the Lab's deterministic local engine. "
        "It provides a structurally correct scaffold and flags where human judgement "
        "or a model-backed engine should be applied to complete the methodology."
    )

    strengths = [
        "Establishes a candidate problem framing (requires human verification).",
        "Provides sufficient text volume for extracting architectural primitives.",
    ]
    gaps = [
        "No automated semantic analysis is performed in local mode; complete sections manually or via a model engine.",
        "Scores are set to 0 by default to avoid implying evidence-backed judgement.",
    ]

    return LocalReview(title=title, year=year, executive_thesis=thesis, strengths=strengths, gaps=gaps)


class LocalEngineAdapter(ReviewEngine):
    """Adapter that exposes the existing local scaffold logic via the engine interface."""

    name = "local"

    def generate(self, *, text: str, pdf_sha256: str, config: EngineConfig) -> EngineResult:
        # Reuse heuristics
        title, year = guess_title_and_year(text)

        metadata: Dict[str, Any] = {
            "title": title,
            "authors": [],
            "published_year": year,
            "source": "local",
            "tags": ["generated", "deterministic", "local-engine"],
        }
        scorecard: Dict[str, Any] = {
            "version": 0.1,
            "paper": {"title": title, "year": year},
            "scores": {
                "tiering_completeness": 0,
                "accountability_plumbing": 0,
                "data_governance": 0,
                "redress": 0,
                "sovereignty": 0,
            },
            "notes": [
                "Local deterministic engine does not infer evidence-backed scores.",
                "Replace 0s with rubric-justified scores after completing sections 1-9 of the review report.",
            ],
        }
        analysis: Dict[str, Any] = {
            "executive_summary": (
                "Deterministic local-engine scaffold. This contains no semantic model judgement; "
                "complete the analysis using the Lab methodology and the extracted paper text."
            ),
            "scope_and_claims": [
                "Identify the paper's stated scope and target audience.",
                "List the main claims in the author's own framing.",
                "Separate normative claims from empirical claims."
            ],
            "methods_and_evidence": [
                "Describe any evaluation methodology used (if any).",
                "List the evidence types (case studies, benchmarks, surveys, etc.).",
                "Note what is asserted without evidence."
            ],
            "assumptions": [
                "Identify implicit assumptions about deployment context.",
                "Identify assumptions about governance actors and incentives.",
                "Identify assumptions about data quality and institutional capacity."
            ],
            "key_terms": [
                {"term": "DPI", "definition": "Define as used by the paper."},
                {"term": "Governance", "definition": "Define as used by the paper."},
                {"term": "Assurance", "definition": "Define as used by the paper."}
            ],
            "notable_quotes": [
                {"quote": "(Add quotes from the paper)", "why_it_matters": "Use as evidence anchors."},
                {"quote": "(Add quotes from the paper)", "why_it_matters": "Use as evidence anchors."}
            ],
        }
        report: Dict[str, Any] = {
            "executive_thesis": (
                "This review was generated using the Lab's deterministic local engine. "
                "It provides a structurally correct scaffold and flags where judgement should be applied."
            ),
            "strengths": [
                "Establishes a candidate problem framing (requires verification).",
                "Provides sufficient text volume for extracting architectural primitives.",
                "Creates a repeatable review directory contract."
            ],
            "gaps_and_omissions": [
                "No automated semantic analysis is performed in local mode.",
                "Claims/evidence mapping must be completed by a reviewer.",
                "Risk tiering and control mapping must be completed by a reviewer.",
                "Scores are placeholders to avoid false certainty.",
                "Redress and accountability pathways must be operationalized."
            ],
            "risk_and_controls": [
                {"risk": "Hallucinated certainty", "why_it_matters": "False confidence harms governance.", "minimal_control": "Require evidence cues for every score."},
                {"risk": "Unscoped deployment", "why_it_matters": "Scope creep increases harms.", "minimal_control": "Mandate explicit context + assumptions."},
                {"risk": "Weak accountability", "why_it_matters": "No one owns outcomes.", "minimal_control": "Define decision rights + audit trails."},
                {"risk": "Data governance gaps", "why_it_matters": "Bad inputs degrade outputs.", "minimal_control": "Specify data provenance and quality checks."},
                {"risk": "No redress", "why_it_matters": "Harms persist without remedy.", "minimal_control": "Define complaint and appeal pathways."}
            ],
            "recommended_minimal_viable_upgrades": [
                {"upgrade": "Evidence-cued score justification", "implementation_hint": "Add a short evidence cue per score.", "expected_impact": "Reduces ungrounded scoring."},
                {"upgrade": "Explicit scope statement", "implementation_hint": "Add a scope section in metadata.", "expected_impact": "Prevents overgeneralization."},
                {"upgrade": "Control mapping", "implementation_hint": "Map gaps to control objectives.", "expected_impact": "Makes remediation actionable."},
                {"upgrade": "Redress workflow", "implementation_hint": "Add a minimal redress diagram.", "expected_impact": "Improves accountability."},
                {"upgrade": "Provenance manifest", "implementation_hint": "Keep hashes and prompts.", "expected_impact": "Enables auditability."}
            ],
            "open_questions": [
                "What are the paper's non-negotiable assumptions?",
                "Which governance actor is expected to enforce controls?",
                "What evidence would change the core conclusions?"
            ],
        }

        return EngineResult(metadata=metadata, scorecard=scorecard, analysis=analysis, report=report, raw={"engine": "local"})

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class EngineConfig:
    """Configuration for a review engine.

    Determinism is driven by:
    - fixed model name
    - temperature=0/top_p=1 (for model-backed engines)
    - stable prompts
    - stable seed derived from input hash (when supported)
    """

    model: str
    seed: int
    max_input_chars: int = 180_000
    # Where applicable; engines may ignore unsupported params.
    temperature: float = 0.0
    top_p: float = 1.0


@dataclass(frozen=True)
class EngineResult:
    """Structured, schema-valid outputs for rendering into repo artifacts."""

    metadata: Dict[str, Any]
    scorecard: Dict[str, Any]
    analysis: Dict[str, Any]
    report: Dict[str, Any]
    # Raw response payloads for audit/debug.
    raw: Dict[str, Any]


class ReviewEngine:
    name: str

    def generate(self, *, text: str, pdf_sha256: str, config: EngineConfig) -> EngineResult:
        raise NotImplementedError

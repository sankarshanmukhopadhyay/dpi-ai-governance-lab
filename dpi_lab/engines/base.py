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

    # Prefer token budgets when available (model engines can be token-aware).
    # If these are None, engines may fall back to character budgets.
    max_input_tokens: Optional[int] = None
    chunk_max_tokens: Optional[int] = None
    max_output_tokens: int = 2048
    repair_retries: int = 1
    max_input_chars: int = 180_000
    # Chunking controls for long inputs (engines may ignore).
    # If the canonicalized paper text exceeds max_input_chars, engines SHOULD
    # switch to deterministic chunking and multi-pass summarization.
    chunk_max_chars: int = 60_000
    chunk_max_count: int = 12
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

    def generate(
        self,
        *,
        text: str,
        pdf_sha256: str,
        config: EngineConfig,
        pages: Optional[list[Dict[str, Any]]] = None,
    ) -> EngineResult:
        raise NotImplementedError

    def semantic_validate(
        self,
        *,
        paper_text: str,
        artifacts: Dict[str, Any],
        pdf_sha256: str,
        config: EngineConfig,
        pages: Optional[list[Dict[str, Any]]] = None,
    ) -> Dict[str, Any]:
        """Optional semantic validation.

        Contract/schema validation is engine-agnostic and runs offline.
        Semantic validation is *optional* and may call a model provider.

        Engines that do not support semantic validation SHOULD raise
        NotImplementedError.
        """

        raise NotImplementedError

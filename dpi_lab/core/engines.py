from __future__ import annotations

from typing import Dict

from dpi_lab.engines.base import ReviewEngine


def get_engine(name: str) -> ReviewEngine:
    name = (name or "").strip().lower()
    if name == "local":
        from dpi_lab.core.local_engine import LocalEngineAdapter

        return LocalEngineAdapter()
    if name == "openai":
        from dpi_lab.engines.openai_engine import OpenAIEngine

        return OpenAIEngine()
    raise ValueError(f"Unsupported engine: {name}")


def list_engines() -> Dict[str, str]:
    return {
        "local": "Deterministic scaffold-only engine (no model calls)",
        "openai": "OpenAI model-backed engine (JSON-first + deterministic rendering)",
    }

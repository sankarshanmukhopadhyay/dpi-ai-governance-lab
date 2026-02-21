from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_schema(rel_path: str) -> Dict[str, Any]:
    """Load a JSON schema from the repository root using a relative path."""

    repo_root = Path(__file__).resolve().parents[2]
    p = repo_root / rel_path
    if not p.exists():
        raise FileNotFoundError(f"Schema not found: {p}")
    return json.loads(p.read_text(encoding="utf-8"))

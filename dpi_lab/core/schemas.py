from __future__ import annotations

import json
from pathlib import Path

from dpi_lab.core.resources import read_text as read_resource_text
from typing import Any, Dict


def load_schema(rel_path: str) -> Dict[str, Any]:
    """Load a JSON schema.

    rel_path is relative to the repository root, e.g.:
      - "schemas/reviews/paper-review-scorecard.schema.json"

    For pip installs, schemas are loaded from packaged resources under dpi_lab/resources/.
    For editable installs, we fall back to repo-relative paths.
    """
    # Prefer packaged resources
    if rel_path.startswith("schemas/"):
        res_rel = rel_path[len("schemas/"):]
        try:
            return json.loads(read_resource_text(f"schemas/{res_rel}", encoding="utf-8"))
        except FileNotFoundError:
            pass

    repo_root = Path(__file__).resolve().parents[2]
    p = repo_root / rel_path
    return json.loads(p.read_text(encoding="utf-8"))

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

from dpi_lab.core.engines import get_engine
from dpi_lab.engines.base import EngineConfig
from dpi_lab.core.utils import safe_write_text


@dataclass
class SemanticValidation:
    errors: List[str]
    warnings: List[str]
    output_path: Optional[Path] = None


def _load_yaml(p: Path) -> Any:
    return yaml.safe_load(p.read_text(encoding="utf-8"))


def _load_md(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")


def _load_manifest_engine(review_dir: Path) -> tuple[str | None, str | None, int | None]:
    man = review_dir / "run" / "manifest.json"
    if not man.exists():
        return None, None, None
    try:
        obj = json.loads(man.read_text(encoding="utf-8"))
        return obj.get("engine"), obj.get("model"), obj.get("seed")
    except Exception:
        return None, None, None


def semantic_validate(
    *,
    review_dir: Path,
    engine: str | None,
    model: str | None,
    max_input_chars: int = 180_000,
    max_input_tokens: int | None = None,
) -> SemanticValidation:
    """Run optional semantic validation using the selected engine.

    This is *not* required for offline determinism. It is an opt-in tier.
    The result is persisted to run/semantic-validation.json.
    """

    review_dir = review_dir.resolve()
    errors: List[str] = []
    warnings: List[str] = []

    manifest_engine, manifest_model, manifest_seed = _load_manifest_engine(review_dir)
    chosen_engine = (engine or manifest_engine or "").strip().lower()
    if not chosen_engine:
        errors.append("No engine specified for semantic validation and no manifest engine found.")
        return SemanticValidation(errors=errors, warnings=warnings)

    if chosen_engine == "local":
        errors.append("Semantic validation requires a model-backed engine; 'local' does not support it.")
        return SemanticValidation(errors=errors, warnings=warnings)

    chosen_model = model or manifest_model or "gpt-5"

    # Load paper text
    extracted = review_dir / "extracted" / "paper.text.v1.txt"
    if not extracted.exists():
        errors.append("Missing extracted paper text (extracted/paper.text.v1.txt); run extraction first.")
        return SemanticValidation(errors=errors, warnings=warnings)
    paper_text = extracted.read_text(encoding="utf-8", errors="replace")

    # Optional pages
    pages = None
    pages_path = review_dir / "extracted" / "paper.pages.v1.json"
    if pages_path.exists():
        try:
            pages = json.loads(pages_path.read_text(encoding="utf-8")).get("pages")
        except Exception:
            pages = None

    # Artifacts bundle (JSON-first input to the semantic validator)
    artifacts: Dict[str, Any] = {}
    meta_p = review_dir / "paper-review-metadata.yaml"
    score_p = review_dir / "paper-review-scorecard.yaml"
    analysis_p = review_dir / "paper-analysis.md"
    report_p = review_dir / "paper-review-report.md"
    if meta_p.exists():
        artifacts["metadata"] = _load_yaml(meta_p)
    if score_p.exists():
        artifacts["scorecard"] = _load_yaml(score_p)
    if analysis_p.exists():
        artifacts["analysis_md"] = _load_md(analysis_p)
    if report_p.exists():
        artifacts["report_md"] = _load_md(report_p)

    # Provenance hash (best effort)
    pdf_sha = ""
    man = review_dir / "run" / "manifest.json"
    if man.exists():
        try:
            pdf_sha = json.loads(man.read_text(encoding="utf-8")).get("inputs", {}).get("pdf_sha256", "")
        except Exception:
            pdf_sha = ""

    seed = manifest_seed if isinstance(manifest_seed, int) else (int(pdf_sha[:8], 16) if pdf_sha else 0)

    cfg = EngineConfig(
        model=chosen_model,
        seed=seed,
        max_input_chars=max_input_chars,
        max_input_tokens=max_input_tokens,
    )

    eng = get_engine(chosen_engine)
    try:
        out = eng.semantic_validate(paper_text=paper_text, artifacts=artifacts, pdf_sha256=pdf_sha, config=cfg, pages=pages)
    except NotImplementedError:
        errors.append(f"Engine '{chosen_engine}' does not implement semantic validation.")
        return SemanticValidation(errors=errors, warnings=warnings)

    # Persist
    run_dir = review_dir / "run"
    run_dir.mkdir(parents=True, exist_ok=True)
    out_path = run_dir / "semantic-validation.json"
    safe_write_text(out_path, json.dumps(out, indent=2, ensure_ascii=False) + "\n")

    data = out.get("data") if isinstance(out, dict) else None
    if isinstance(data, dict):
        issues = data.get("issues", [])
        for it in issues if isinstance(issues, list) else []:
            if not isinstance(it, dict):
                continue
            sev = it.get("severity", "warning")
            msg = it.get("message", "")
            code = it.get("code", "")
            artifact = it.get("artifact", "unknown")
            line = f"semantic:{sev}:{code}:{artifact}: {msg}".strip()
            if sev == "error":
                errors.append(line)
            else:
                warnings.append(line)
    else:
        warnings.append("semantic:warning:unstructured:unknown: Semantic validator returned no 'data' object")

    return SemanticValidation(errors=errors, warnings=warnings, output_path=out_path)

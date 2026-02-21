from __future__ import annotations

import json
import os
from typing import Any, Dict

from jsonschema import validate as js_validate

from dpi_lab.core.schemas import load_schema
from dpi_lab.engines.base import EngineConfig, EngineResult, ReviewEngine


class OpenAIEngine(ReviewEngine):
    """Model-backed engine using the OpenAI Responses API.

    Design goal: JSON-first. We ask the model for schema-conforming JSON, then
    deterministically render repo artifacts from that JSON.

    Notes on determinism:
    - We set temperature=0/top_p=1.
    - We pass a seed derived from the input hash when supported.
    - Even then, absolute determinism is not guaranteed across time/model
      revisions; we therefore always persist prompts + raw responses.
    """

    name = "openai"

    def __init__(self) -> None:
        try:
            from openai import OpenAI  # type: ignore
        except Exception as e:  # pragma: no cover
            raise RuntimeError(
                "Missing dependency 'openai'. Install requirements.txt before using engine=openai."
            ) from e

        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY is not set. Export it in your shell before running dpi-lab with --engine openai."
            )

        base_url = os.getenv("OPENAI_BASE_URL")
        if base_url:
            self.client = OpenAI(api_key=api_key, base_url=base_url)
        else:
            self.client = OpenAI(api_key=api_key)

    def _call(self, *, prompt: str, schema_name: str, schema: Dict[str, Any], config: EngineConfig) -> Dict[str, Any]:
        """Single deterministic schema-constrained call."""

        response_format = {
            "type": "json_schema",
            "json_schema": {
                "name": schema_name,
                "description": f"Return strictly valid JSON for {schema_name}.",
                "schema": schema,
                "strict": True,
            },
        }

        # Responses API input can be a string or message list.
        # We keep it as a single instruction-rich user message to reduce variability.
        payload = self.client.responses.create(
            model=config.model,
            input=prompt,
            temperature=config.temperature,
            top_p=config.top_p,
            seed=config.seed,
            response_format=response_format,
        )

        # The SDK returns a structured object; extract a JSON string.
        # The Responses API exposes output items; the SDK also offers output_text convenience.
        out_text = getattr(payload, "output_text", None)
        if callable(out_text):
            out = out_text()
        else:
            out = getattr(payload, "output_text", "")

        if not out:
            # Fallback: attempt to serialize payload and hunt for text
            out = json.dumps(getattr(payload, "model_dump", lambda: payload)(), ensure_ascii=False)

        data = json.loads(out)
        js_validate(instance=data, schema=schema)
        return {"data": data, "raw": getattr(payload, "model_dump", lambda: payload)()}

    def generate(self, *, text: str, pdf_sha256: str, config: EngineConfig) -> EngineResult:
        # Truncate deterministically to protect token budgets while keeping replay stable.
        clipped = text[: config.max_input_chars]

        # Load schemas
        meta_schema = load_schema("schemas/reviews/paper-review-metadata.schema.json")
        score_schema = load_schema("schemas/reviews/paper-review-scorecard.schema.json")
        analysis_schema = load_schema("schemas/reviews/paper-analysis.schema.json")
        report_schema = load_schema("schemas/reviews/paper-review-report.schema.json")

        common_header = (
            "You are a strict evaluator operating the DPI AI Governance Lab methodology. "
            "Use only the provided paper text; do not invent citations or claims not supported by the text. "
            "Be specific, operational, and map claims to concrete gaps and risks. "
            "Return ONLY JSON matching the supplied schema."\
        )
        context = (
            f"Paper content (canonicalized excerpt; sha256={pdf_sha256}):\n"  # stable provenance
            "-----BEGIN PAPER TEXT-----\n"
            f"{clipped}\n"
            "-----END PAPER TEXT-----\n"
        )

        # 1) Metadata
        meta_prompt = (
            f"{common_header}\n\n"
            "Task: Produce paper-review-metadata JSON.\n"
            "Guidance: title should be the paper title if inferable; published_year should be an integer year if inferable else 0; "
            "authors may be empty if unclear; tags should be short, lower_snake_case.\n\n"
            + context
        )
        meta = self._call(prompt=meta_prompt, schema_name="paper_review_metadata", schema=meta_schema, config=config)

        # 2) Scorecard
        score_prompt = (
            f"{common_header}\n\n"
            "Task: Produce paper-review-scorecard JSON.\n"
            "Scoring: integer 0..5 where 0=not addressed, 3=adequate, 5=excellent, based on evidence in the text. "
            "Include notes that justify scores with short evidence cues (no line numbers needed).\n\n"
            + context
        )
        score = self._call(prompt=score_prompt, schema_name="paper_review_scorecard", schema=score_schema, config=config)

        # 3) Analysis (structured)
        analysis_prompt = (
            f"{common_header}\n\n"
            "Task: Produce paper-analysis JSON.\n"
            "Guidance: be concise but concrete; emphasize assumptions, scope, methods, and claims vs evidence.\n\n"
            + context
        )
        analysis = self._call(prompt=analysis_prompt, schema_name="paper_analysis", schema=analysis_schema, config=config)

        # 4) Report (structured)
        report_prompt = (
            f"{common_header}\n\n"
            "Task: Produce paper-review-report JSON.\n"
            "Guidance: include executive thesis, strengths, gaps/omissions, redress/accountability notes, and recommended minimal viable upgrades.\n\n"
            + context
        )
        report = self._call(prompt=report_prompt, schema_name="paper_review_report", schema=report_schema, config=config)

        raw = {
            "metadata": meta["raw"],
            "scorecard": score["raw"],
            "analysis": analysis["raw"],
            "report": report["raw"],
            "prompts": {
                "metadata": meta_prompt,
                "scorecard": score_prompt,
                "analysis": analysis_prompt,
                "report": report_prompt,
            },
        }

        return EngineResult(
            metadata=meta["data"],
            scorecard=score["data"],
            analysis=analysis["data"],
            report=report["data"],
            raw=raw,
        )

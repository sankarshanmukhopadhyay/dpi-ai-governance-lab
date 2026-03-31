
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

import yaml

SCORE_KEYS = ["tiering_completeness", "accountability_plumbing", "data_governance", "redress", "sovereignty"]


def _load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def find_review_dirs(root: Path) -> List[Path]:
    root = root.resolve()
    if (root / "paper-review-scorecard.yaml").exists() and (root / "paper-review-metadata.yaml").exists():
        return [root]
    dirs = sorted({p.parent.resolve() for p in root.rglob("paper-review-scorecard.yaml")})
    return [d for d in dirs if (d / "paper-review-metadata.yaml").exists()]


def build_comparison(root: Path) -> Dict[str, Any]:
    review_dirs = find_review_dirs(root)
    reviews: List[Dict[str, Any]] = []
    totals = {k: 0 for k in SCORE_KEYS}

    for d in review_dirs:
        metadata = _load_yaml(d / "paper-review-metadata.yaml")
        scorecard = _load_yaml(d / "paper-review-scorecard.yaml")
        scores = scorecard.get("scores", {})
        total = sum(int(scores.get(k, 0)) for k in SCORE_KEYS)
        for key in SCORE_KEYS:
            totals[key] += int(scores.get(key, 0))
        reviews.append({
            "review_dir": str(d),
            "title": metadata.get("title", scorecard.get("paper", {}).get("title", "Untitled")),
            "published_year": metadata.get("published_year", scorecard.get("paper", {}).get("year")),
            "source": metadata.get("source", ""),
            "tags": metadata.get("tags", []),
            "scores": {k: int(scores.get(k, 0)) for k in SCORE_KEYS},
            "total_score": total,
            "notes": scorecard.get("notes", []),
        })

    review_count = len(reviews)
    averages = {k: round((totals[k] / review_count), 2) if review_count else 0.0 for k in SCORE_KEYS}
    reviews.sort(key=lambda x: (-x["total_score"], str(x["title"])))
    return {
        "comparison_type": "dpi-ai-governance-lab.review-comparison",
        "comparison_version": 1,
        "review_count": review_count,
        "score_keys": SCORE_KEYS,
        "averages": averages,
        "reviews": reviews,
    }


def render_comparison_markdown(data: Dict[str, Any]) -> str:
    lines = [
        "# Comparative review matrix",
        "",
        f"Reviews included: **{data['review_count']}**",
        "",
        "## Average scores",
        "",
    ]
    for key, value in data["averages"].items():
        lines.append(f"- **{key}**: {value}")
    lines.extend([
        "",
        "## Paper comparison",
        "",
        "| Paper | Year | Tiering | Accountability | Data | Redress | Sovereignty | Total |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ])
    for item in data["reviews"]:
        s = item["scores"]
        lines.append(
            f"| {item['title']} | {item.get('published_year','')} | {s['tiering_completeness']} | {s['accountability_plumbing']} | {s['data_governance']} | {s['redress']} | {s['sovereignty']} | {item['total_score']} |"
        )
    lines.extend(["", "## Notes", ""])
    for item in data["reviews"]:
        lines.append(f"### {item['title']}")
        lines.append(f"- Source: {item.get('source','')}" if item.get("source") else "- Source: n/a")
        lines.append(f"- Tags: {', '.join(item.get('tags', []))}" if item.get("tags") else "- Tags: n/a")
        notes = item.get("notes") or []
        if notes:
            for note in notes:
                lines.append(f"- Note: {note}")
        else:
            lines.append("- Note: none recorded")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def write_comparison(root: Path, out_path: Path) -> Dict[str, Path]:
    data = build_comparison(root)
    out_path = out_path.resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    json_path = out_path.with_suffix(".json")
    md_path = out_path.with_suffix(".md")
    json_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_path.write_text(render_comparison_markdown(data), encoding="utf-8")
    return {"json": json_path, "markdown": md_path}

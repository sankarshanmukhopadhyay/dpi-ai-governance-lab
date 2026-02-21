from __future__ import annotations

from typing import Any, Dict, List


def _md_list(items: List[str]) -> str:
    return "\n".join([f"- {x}" for x in items]) + "\n"


def render_analysis_md(data: Dict[str, Any]) -> str:
    kt = data.get("key_terms", [])
    quotes = data.get("notable_quotes", [])

    key_terms_md = "\n".join([f"- **{x['term']}**: {x['definition']}" for x in kt]) + "\n"
    quotes_md = "\n".join([f"- “{x['quote']}” — {x['why_it_matters']}" for x in quotes]) + "\n"

    return (
        "# Paper Analysis\n\n"
        "## Executive summary\n"
        f"{data['executive_summary'].strip()}\n\n"
        "## Scope and claims\n"
        f"{_md_list(data['scope_and_claims'])}\n"
        "## Methods and evidence\n"
        f"{_md_list(data['methods_and_evidence'])}\n"
        "## Assumptions\n"
        f"{_md_list(data['assumptions'])}\n"
        "## Key terms\n"
        f"{key_terms_md}\n"
        "## Notable quotes\n"
        f"{quotes_md}"
    )


def render_report_md(data: Dict[str, Any]) -> str:
    rac = data.get("risk_and_controls", [])
    mvu = data.get("recommended_minimal_viable_upgrades", [])

    rac_md = "\n".join(
        [
            f"- **Risk:** {x['risk']}\n  - Why it matters: {x['why_it_matters']}\n  - Minimal control: {x['minimal_control']}"
            for x in rac
        ]
    )
    mvu_md = "\n".join(
        [
            f"- **Upgrade:** {x['upgrade']}\n  - Implementation hint: {x['implementation_hint']}\n  - Expected impact: {x['expected_impact']}"
            for x in mvu
        ]
    )

    return (
        "# Paper review report\n\n"
        "## Executive thesis\n"
        f"{data['executive_thesis'].strip()}\n\n"
        "## Strengths\n"
        f"{_md_list(data['strengths'])}\n"
        "## Gaps and omissions\n"
        f"{_md_list(data['gaps_and_omissions'])}\n"
        "## Risk and minimal controls\n"
        f"{rac_md}\n\n"
        "## Recommended minimal viable upgrades\n"
        f"{mvu_md}\n\n"
        "## Open questions\n"
        f"{_md_list(data['open_questions'])}"
    )

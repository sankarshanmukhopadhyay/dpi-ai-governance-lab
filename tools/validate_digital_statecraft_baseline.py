from collections import Counter
from pathlib import Path
import sys
import yaml

REVIEWS = Path("reviews/digital-statecraft-dpi")
BASELINE = Path("baselines/digital-statecraft-dpi-2026")


def main() -> int:
    errors = []
    observed = Counter()
    total = 0
    standardized = 0
    none = 0
    for path in sorted(REVIEWS.glob("*/governance-gaps.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        for gap in data.get("gaps", []):
            total += 1
            cap = gap["required_capability"]["id"]
            observed[cap] += 1
            coverage = gap["remediation"]["coverage"]
            standardized += coverage == "standardized"
            none += coverage == "none"
    recurring = yaml.safe_load((BASELINE / "recurring-gaps.yaml").read_text(encoding="utf-8"))
    declared = {item["capability_id"]: item["gap_count"] for item in recurring["capabilities"]}
    if dict(observed) != declared:
        errors.append(f"recurrence mismatch: observed={dict(observed)} declared={declared}")
    coverage = yaml.safe_load((BASELINE / "capability-coverage.yaml").read_text(encoding="utf-8"))
    metrics = coverage["metrics"]
    if total != metrics["material_gaps"]:
        errors.append("material gap count mismatch")
    if standardized != metrics["gaps_with_standardized_remediation"]:
        errors.append("standardized gap count mismatch")
    if none != metrics["gaps_with_no_registered_remediation"]:
        errors.append("no-coverage gap count mismatch")
    if metrics["gaps_with_partial_remediation"] != 0:
        errors.append("first-wave baseline expects zero partial mappings")
    expected_ratio = round(standardized / total, 4)
    if metrics["artifact_coverage_ratio"] != expected_ratio or metrics["standardized_remediation_ratio"] != expected_ratio:
        errors.append("coverage ratio mismatch")
    demands = yaml.safe_load((BASELINE / "artifact-demand.yaml").read_text(encoding="utf-8"))["demands"]
    demand_caps = {item["capability_id"] for item in demands}
    expected_demand = {cap for cap, count in observed.items() if cap in {"CAP-INFERENCE-TRACEABILITY", "CAP-CORRECTION-PROPAGATION", "CAP-INTERINSTITUTIONAL-ADMISSIBILITY"}}
    if demand_caps != expected_demand:
        errors.append(f"artifact demand mismatch: {demand_caps} != {expected_demand}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 2
    print(f"Digital Statecraft baseline OK: {total} gaps, {len(observed)} capabilities, {standardized} standardized, {none} unmet")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

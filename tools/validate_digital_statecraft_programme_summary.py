#!/usr/bin/env python3
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "baselines" / "digital-statecraft-dpi-2026" / "programme-summary.yaml"
BASELINE = ROOT / "baselines" / "digital-statecraft-dpi-2026" / "capability-coverage.yaml"
CLOSURE = ROOT / "case-studies" / "digital-statecraft-benefit-closure" / "closure-evidence.yaml"


def fail(errors):
    for error in errors:
        print(f"FAIL: {error}")
    return 2


def main() -> int:
    errors = []
    for path in (SUMMARY, BASELINE, CLOSURE):
        if not path.exists():
            errors.append(f"missing required evidence file: {path.relative_to(ROOT)}")
    if errors:
        return fail(errors)

    summary = yaml.safe_load(SUMMARY.read_text(encoding="utf-8"))
    baseline = yaml.safe_load(BASELINE.read_text(encoding="utf-8"))
    closure = yaml.safe_load(CLOSURE.read_text(encoding="utf-8"))

    corpus = summary.get("corpus", {})
    historical = summary.get("historical_baseline", {})
    current = summary.get("current_remediation", {})
    fixture = summary.get("worked_fixture", {})
    publication = summary.get("publication_level_closure", {})

    if corpus.get("publications") != 6 or corpus.get("trace_reviews") != 6:
        errors.append("programme summary must report six publications and six TRACE reviews")
    if corpus.get("material_gaps") != 19 or corpus.get("recurring_capability_classes") != 6:
        errors.append("programme summary must report 19 gaps across six recurring capability classes")

    # The historical baseline is immutable and remains the source of the before-state claim.
    metrics = baseline.get("metrics", baseline)
    historical_standardized = metrics.get("standardized_remediation_gaps", metrics.get("standardized_gap_mappings"))
    historical_none = metrics.get("no_registered_remediation", metrics.get("no_coverage_gaps"))
    if historical.get("standardized_gap_mappings") != 10 or historical.get("no_registered_remediation") != 9:
        errors.append("historical summary must preserve 10 standardized / 9 uncovered mappings")
    if round(float(historical.get("standardized_coverage_ratio", 0)), 4) != 0.5263:
        errors.append("historical standardized coverage must remain 0.5263")
    if historical_standardized is not None and historical_standardized != 10:
        errors.append("programme summary disagrees with historical baseline standardized count")
    if historical_none is not None and historical_none != 9:
        errors.append("programme summary disagrees with historical baseline uncovered count")

    if current.get("standardized_capability_classes") != 6 or current.get("first_wave_gap_mappings") != 19:
        errors.append("current remediation summary must report six standardized capabilities and 19 mappings")
    if float(current.get("standardized_coverage_ratio", 0)) != 1.0:
        errors.append("current remediation coverage must be 1.0")

    if fixture.get("selected_capabilities") != 6 or fixture.get("selected_capabilities_passed") != 6:
        errors.append("worked fixture must report 6/6 selected capability passes")
    if fixture.get("scenarios_executed") != 9 or fixture.get("negative_scenarios") != 8:
        errors.append("worked fixture must report nine scenarios including eight negative scenarios")
    if fixture.get("closure_status") != "closed":
        errors.append("worked fixture closure status must be closed")

    closure_status = closure.get("closure_status", closure.get("status"))
    if closure_status and closure_status != "closed":
        errors.append("programme summary disagrees with fixture closure evidence")

    if publication.get("closed_publication_gaps") != 0:
        errors.append("synthetic fixture must not close publication-level gaps")

    derived = summary.get("new_evidence_derived_capabilities", [])
    expected = {
        "CAP-INFERENCE-TRACEABILITY",
        "CAP-CORRECTION-PROPAGATION",
        "CAP-INTERINSTITUTIONAL-ADMISSIBILITY",
    }
    if set(derived) != expected:
        errors.append("evidence-derived capability list does not match the three corpus-derived additions")

    if errors:
        return fail(errors)

    print("Digital Statecraft programme summary OK")
    print("Historical coverage: 10/19 (52.63%)")
    print("Current remediation mapping: 19/19 (100%)")
    print("Synthetic capability closure: 6/6")
    print("Publication-level closures: 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

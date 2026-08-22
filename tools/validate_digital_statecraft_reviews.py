from pathlib import Path
import sys
import yaml

ROOT = Path("reviews/digital-statecraft-dpi")
EXPECTED = {
    "a-first-principles-case-for-dpi-ai": "DS-TRACE-001",
    "minimum-digital-kernel": "DS-TRACE-002",
    "governance-stack": "DS-TRACE-003",
    "digital-constitution": "DS-TRACE-004",
    "fast-and-fair-decisions": "DS-TRACE-005",
    "trust-travels-between-institutions": "DS-TRACE-006",
}


def main() -> int:
    errors = []
    total_gaps = 0
    standardized = 0
    unmet = 0
    versions = set()
    seen_review_ids = set()
    for slug, review_id in EXPECTED.items():
        directory = ROOT / slug
        for filename in ("metadata.yaml", "review-report.md", "scorecard.yaml", "governance-gaps.yaml"):
            if not (directory / filename).exists():
                errors.append(f"{slug}: missing {filename}")
        if not (directory / "metadata.yaml").exists():
            continue
        metadata = yaml.safe_load((directory / "metadata.yaml").read_text(encoding="utf-8"))
        if metadata.get("review_id") != review_id:
            errors.append(f"{slug}: review_id mismatch")
        if metadata.get("corpus_id") != "digital-statecraft-dpi-2026-wave1":
            errors.append(f"{slug}: corpus_id mismatch")
        if metadata.get("methodology") != "TRACE":
            errors.append(f"{slug}: methodology must be TRACE")
        versions.add(str(metadata.get("methodology_version")))
        if review_id in seen_review_ids:
            errors.append(f"duplicate review id {review_id}")
        seen_review_ids.add(review_id)
        scorecard = yaml.safe_load((directory / "scorecard.yaml").read_text(encoding="utf-8"))
        for key, value in scorecard.get("scores", {}).items():
            if not isinstance(value, int) or not 0 <= value <= 5:
                errors.append(f"{slug}: score {key} outside 0..5")
        gaps = yaml.safe_load((directory / "governance-gaps.yaml").read_text(encoding="utf-8"))
        if gaps.get("review_id") != review_id:
            errors.append(f"{slug}: governance gap review_id mismatch")
        for gap in gaps.get("gaps", []):
            total_gaps += 1
            coverage = gap.get("remediation", {}).get("coverage")
            if coverage == "standardized":
                standardized += 1
            elif coverage == "none":
                unmet += 1
    if versions != {"0.7.0"}:
        errors.append(f"all reviews must use TRACE 0.7.0; saw {sorted(versions)}")
    if total_gaps != 19:
        errors.append(f"expected 19 material gaps, found {total_gaps}")
    if standardized != 10 or unmet != 9:
        errors.append(f"expected standardized/unmet 10/9, found {standardized}/{unmet}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 2
    print(f"Digital Statecraft reviews OK: {len(EXPECTED)} reviews, {total_gaps} gaps, {standardized} standardized, {unmet} unmet")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

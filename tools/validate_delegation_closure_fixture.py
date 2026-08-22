from __future__ import annotations

from datetime import datetime
from pathlib import Path
import yaml

ROOT = Path("case-studies/delegated-entitlement-closure")


def parse(ts: str | datetime) -> datetime:
    if isinstance(ts, datetime):
        return ts
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def decide(delegation: dict, request: dict) -> tuple[str, str]:
    status = request.get("delegation_status", delegation["status"])
    if status == "revoked":
        return "deny", "delegation_revoked"
    if status == "suspended":
        return "deny", "delegation_suspended"
    at = parse(request["at"])
    if at < parse(delegation["validity"]["not_before"]):
        return "deny", "delegation_not_yet_valid"
    if at > parse(delegation["validity"]["not_after"]):
        return "deny", "delegation_expired"
    if request["actor"] != delegation["delegate"]:
        return "deny", "delegate_mismatch"
    scope = delegation["scope"]
    if request["action"] not in scope["actions"]:
        return "deny", "action_out_of_scope"
    if request["resource"] not in scope["resources"]:
        return "deny", "resource_out_of_scope"
    if request["purpose"] not in scope["purposes"]:
        return "deny", "purpose_out_of_scope"
    return "allow", "delegation_valid"


def main() -> int:
    delegation = yaml.safe_load((ROOT / "delegation-record.yaml").read_text(encoding="utf-8"))
    requests = yaml.safe_load((ROOT / "authorization-requests.yaml").read_text(encoding="utf-8"))["requests"]
    records = yaml.safe_load((ROOT / "runtime-authorization-records.yaml").read_text(encoding="utf-8"))["records"]
    closure = yaml.safe_load((ROOT / "closure-evidence.yaml").read_text(encoding="utf-8"))

    failures: list[str] = []
    if len(records) != len(requests):
        failures.append("request/authorization-record cardinality mismatch")

    for request, record in zip(requests, records):
        actual = decide(delegation, request)
        expected = (request["expected"]["decision"], request["expected"]["reason"])
        recorded = (record["decision"], record["reason_codes"][0])
        if actual != expected:
            failures.append(f"{request['id']}: expected {expected}, computed {actual}")
        if recorded != expected:
            failures.append(f"{request['id']}: record {recorded} does not match expected {expected}")
        expected_effect = request["expected"].get("effect_id")
        if expected_effect != record.get("effect_id"):
            failures.append(f"{request['id']}: effect correlation mismatch")
        print(f"{request['id']}: {actual[0]} ({actual[1]})")

    required_reasons = {"action_out_of_scope", "purpose_out_of_scope", "delegation_revoked", "delegation_expired"}
    seen_reasons = {record["reason_codes"][0] for record in records if record["decision"] == "deny"}
    if not required_reasons.issubset(seen_reasons):
        failures.append(f"missing negative-path evidence: {sorted(required_reasons - seen_reasons)}")

    if closure.get("status") != "closed":
        failures.append("closure status must be closed for this fixture")
    if any(item.get("result") != "pass" for item in closure.get("acceptance_criteria", [])):
        failures.append("all fixture acceptance criteria must pass")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 2
    print("Delegated entitlement closure fixture: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

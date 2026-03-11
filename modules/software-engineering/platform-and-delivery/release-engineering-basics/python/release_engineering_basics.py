from __future__ import annotations


def required_release_gates(change_tags: list[str]) -> list[str]:
    normalized_tags = {tag.strip().lower() for tag in change_tags if tag.strip()}
    gates = ["build", "tests", "rollback-plan"]
    if normalized_tags.intersection({"database", "migration"}):
        gates.append("migration-review")
    if normalized_tags.intersection({"api", "schema"}):
        gates.append("compatibility-check")
    return gates


def release_blockers(required_gates: list[str], gate_statuses: dict[str, str]) -> list[str]:
    blockers: list[str] = []
    for gate in required_gates:
        if gate_statuses.get(gate) != "passed":
            blockers.append(gate)
    return blockers


def releasable(required_gates: list[str], gate_statuses: dict[str, str]) -> bool:
    return not release_blockers(required_gates, gate_statuses)

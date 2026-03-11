from __future__ import annotations


def rollback_blockers(flagged: bool, reversible_schema: bool, canary: bool) -> list[str]:
    blockers: list[str] = []
    if not flagged:
        blockers.append("no-feature-flag")
    if not reversible_schema:
        blockers.append("irreversible-schema")
    if not canary:
        blockers.append("no-canary")
    return blockers


def rollback_ready(flagged: bool, reversible_schema: bool, canary: bool) -> bool:
    return not rollback_blockers(flagged, reversible_schema, canary)


def rollback_risk(flagged: bool, reversible_schema: bool, canary: bool) -> str:
    blocker_count = len(rollback_blockers(flagged, reversible_schema, canary))
    if blocker_count >= 2:
        return "high"
    if blocker_count == 1:
        return "medium"
    return "low"

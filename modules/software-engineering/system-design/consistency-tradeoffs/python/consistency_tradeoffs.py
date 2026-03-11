from __future__ import annotations


def consistency_mode(cross_entity_invariant: bool, stale_reads_tolerable: bool) -> str:
    if cross_entity_invariant and not stale_reads_tolerable:
        return "strong"
    if stale_reads_tolerable:
        return "eventual"
    return "session"


def read_write_conflict_risk(concurrent_writers: int, stale_reads_tolerable: bool) -> str:
    if concurrent_writers < 0:
        raise ValueError("concurrent_writers must be non-negative")
    if concurrent_writers <= 1:
        return "low"
    if stale_reads_tolerable:
        return "medium"
    return "high"


def consistency_decision(
    cross_entity_invariant: bool,
    stale_reads_tolerable: bool,
    concurrent_writers: int,
) -> str:
    mode = consistency_mode(cross_entity_invariant, stale_reads_tolerable)
    risk = read_write_conflict_risk(concurrent_writers, stale_reads_tolerable)
    if mode == "strong":
        return "protect invariants with strong coordination"
    if mode == "eventual" and risk == "low":
        return "accept async replication and repair"
    if mode == "eventual":
        return "add conflict resolution for async writes"
    return "use session guarantees and careful retry rules"

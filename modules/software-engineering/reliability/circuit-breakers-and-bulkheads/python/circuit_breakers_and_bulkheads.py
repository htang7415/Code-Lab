from __future__ import annotations


def circuit_state(consecutive_failures: int, failure_threshold: int, cooldown_complete: bool) -> str:
    if consecutive_failures < 0 or failure_threshold <= 0:
        raise ValueError("failure counts must be non-negative and threshold positive")
    if consecutive_failures < failure_threshold:
        return "closed"
    if cooldown_complete:
        return "half-open"
    return "open"


def allow_dependency_call(state: str, probe_budget: int = 0) -> bool:
    normalized_state = state.strip().lower()
    if normalized_state == "closed":
        return True
    if normalized_state == "open":
        return False
    if normalized_state == "half-open":
        return probe_budget > 0
    raise ValueError("state must be closed, open, or half-open")


def bulkhead_available(active_work: int, capacity: int) -> bool:
    if active_work < 0 or capacity <= 0:
        raise ValueError("active_work must be non-negative and capacity positive")
    return active_work < capacity

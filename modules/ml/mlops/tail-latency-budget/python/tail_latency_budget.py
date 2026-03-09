from __future__ import annotations


def tail_latency_budget_status(observed_tail_ms: float, budget_ms: float) -> tuple[float, float]:
    if observed_tail_ms < 0.0:
        raise ValueError("observed_tail_ms must be non-negative")
    if budget_ms <= 0.0:
        raise ValueError("budget_ms must be positive")

    budget_usage = observed_tail_ms / budget_ms
    remaining_fraction = max(0.0, 1.0 - budget_usage)
    return budget_usage, remaining_fraction

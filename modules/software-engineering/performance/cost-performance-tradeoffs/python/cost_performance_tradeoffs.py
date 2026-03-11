from __future__ import annotations


def cost_per_1k_requests(hourly_cost: float, requests_per_hour: int) -> float:
    if hourly_cost < 0 or requests_per_hour <= 0:
        raise ValueError("hourly_cost must be non-negative and requests_per_hour positive")
    return (hourly_cost / requests_per_hour) * 1000


def latency_improvement_ms(baseline_ms: int, candidate_ms: int) -> int:
    if baseline_ms < 0 or candidate_ms < 0:
        raise ValueError("latencies must be non-negative")
    return baseline_ms - candidate_ms


def worthwhile_tradeoff(
    latency_gain_ms: int,
    extra_cost_per_1k: float,
    max_extra_cost_per_1k: float,
) -> bool:
    if latency_gain_ms < 0 or extra_cost_per_1k < 0 or max_extra_cost_per_1k < 0:
        raise ValueError("inputs must be non-negative")
    if latency_gain_ms == 0:
        return False
    return extra_cost_per_1k <= max_extra_cost_per_1k

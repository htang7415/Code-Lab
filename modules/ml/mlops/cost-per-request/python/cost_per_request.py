from __future__ import annotations


def cost_per_request(total_cost: float, request_count: int) -> float:
    if total_cost < 0.0:
        raise ValueError("total_cost must be non-negative")
    if request_count <= 0:
        raise ValueError("request_count must be positive")

    return total_cost / request_count

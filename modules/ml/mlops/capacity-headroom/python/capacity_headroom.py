from __future__ import annotations


def capacity_headroom(current_load: float, max_capacity: float) -> tuple[float, float]:
    if current_load < 0.0:
        raise ValueError("current_load must be non-negative")
    if max_capacity <= 0.0:
        raise ValueError("max_capacity must be positive")

    utilization = current_load / max_capacity
    headroom = max(0.0, 1.0 - utilization)
    return utilization, headroom

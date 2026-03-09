from __future__ import annotations


def queue_utilization(queue_depth: int, queue_capacity: int) -> tuple[float, bool]:
    if queue_depth < 0:
        raise ValueError("queue_depth must be non-negative")
    if queue_capacity <= 0:
        raise ValueError("queue_capacity must be positive")

    utilization = queue_depth / queue_capacity
    return utilization, queue_depth >= queue_capacity

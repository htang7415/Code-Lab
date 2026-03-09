from __future__ import annotations

import math


def log_event_rate(event_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if event_count < 0:
        raise ValueError("event_count must be non-negative")
    if event_count > total_count:
        raise ValueError("event_count cannot exceed total_count")
    if event_count == 0:
        return float("-inf")
    return math.log(event_count / total_count)

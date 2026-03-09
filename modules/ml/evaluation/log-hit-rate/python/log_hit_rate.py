from __future__ import annotations

import math


def log_hit_rate(hit_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if hit_count < 0:
        raise ValueError("hit_count must be non-negative")
    if hit_count > total_count:
        raise ValueError("hit_count cannot exceed total_count")
    if hit_count == 0:
        return float("-inf")
    return math.log(hit_count / total_count)

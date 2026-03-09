from __future__ import annotations

import math


def log_miss_rate(miss_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if miss_count < 0:
        raise ValueError("miss_count must be non-negative")
    if miss_count > total_count:
        raise ValueError("miss_count cannot exceed total_count")
    if miss_count == 0:
        return float("-inf")
    return math.log(miss_count / total_count)

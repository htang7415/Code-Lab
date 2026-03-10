from __future__ import annotations

import math


def log_drop_rate(drop_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if drop_count < 0:
        raise ValueError("drop_count must be non-negative")
    if drop_count > total_count:
        raise ValueError("drop_count cannot exceed total_count")
    if drop_count == 0:
        return float("-inf")
    return math.log(drop_count / total_count)

from __future__ import annotations

import math


def log_reject_rate(reject_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if reject_count < 0:
        raise ValueError("reject_count must be non-negative")
    if reject_count > total_count:
        raise ValueError("reject_count cannot exceed total_count")
    if reject_count == 0:
        return float("-inf")
    return math.log(reject_count / total_count)

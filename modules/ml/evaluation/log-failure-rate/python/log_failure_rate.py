from __future__ import annotations

import math


def log_failure_rate(failure_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if failure_count < 0:
        raise ValueError("failure_count must be non-negative")
    if failure_count > total_count:
        raise ValueError("failure_count cannot exceed total_count")
    if failure_count == 0:
        return float("-inf")
    return math.log(failure_count / total_count)

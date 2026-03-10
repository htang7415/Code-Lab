from __future__ import annotations

import math


def log_timeout_rate(timeout_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if timeout_count < 0:
        raise ValueError("timeout_count must be non-negative")
    if timeout_count > total_count:
        raise ValueError("timeout_count cannot exceed total_count")
    if timeout_count == 0:
        return float("-inf")
    return math.log(timeout_count / total_count)

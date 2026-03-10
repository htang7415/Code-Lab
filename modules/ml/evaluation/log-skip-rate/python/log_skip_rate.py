from __future__ import annotations

import math


def log_skip_rate(skip_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if skip_count < 0:
        raise ValueError("skip_count must be non-negative")
    if skip_count > total_count:
        raise ValueError("skip_count cannot exceed total_count")
    if skip_count == 0:
        return float("-inf")
    return math.log(skip_count / total_count)

from __future__ import annotations

import math


def log_error_rate(error_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if error_count < 0:
        raise ValueError("error_count must be non-negative")
    if error_count > total_count:
        raise ValueError("error_count cannot exceed total_count")
    if error_count == 0:
        return float("-inf")
    return math.log(error_count / total_count)

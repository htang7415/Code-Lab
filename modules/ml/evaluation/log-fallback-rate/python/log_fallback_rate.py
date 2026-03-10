from __future__ import annotations

import math


def log_fallback_rate(fallback_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if fallback_count < 0:
        raise ValueError("fallback_count must be non-negative")
    if fallback_count > total_count:
        raise ValueError("fallback_count cannot exceed total_count")
    if fallback_count == 0:
        return float("-inf")
    return math.log(fallback_count / total_count)

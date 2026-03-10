from __future__ import annotations

import math


def log_bypass_rate(bypass_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if bypass_count < 0:
        raise ValueError("bypass_count must be non-negative")
    if bypass_count > total_count:
        raise ValueError("bypass_count cannot exceed total_count")
    if bypass_count == 0:
        return float("-inf")
    return math.log(bypass_count / total_count)

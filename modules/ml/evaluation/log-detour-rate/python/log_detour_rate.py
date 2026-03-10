from __future__ import annotations

import math


def log_detour_rate(detour_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if detour_count < 0:
        raise ValueError("detour_count must be non-negative")
    if detour_count > total_count:
        raise ValueError("detour_count cannot exceed total_count")
    if detour_count == 0:
        return float("-inf")
    return math.log(detour_count / total_count)

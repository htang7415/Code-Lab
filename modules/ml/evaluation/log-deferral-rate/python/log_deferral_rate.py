from __future__ import annotations

import math


def log_deferral_rate(deferral_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if deferral_count < 0:
        raise ValueError("deferral_count must be non-negative")
    if deferral_count > total_count:
        raise ValueError("deferral_count cannot exceed total_count")
    if deferral_count == 0:
        return float("-inf")
    return math.log(deferral_count / total_count)

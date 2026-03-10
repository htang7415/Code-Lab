from __future__ import annotations

import math


def log_defect_rate(defect_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if defect_count < 0:
        raise ValueError("defect_count must be non-negative")
    if defect_count > total_count:
        raise ValueError("defect_count cannot exceed total_count")
    if defect_count == 0:
        return float("-inf")
    return math.log(defect_count / total_count)

from __future__ import annotations

import math


def log_abandon_rate(abandon_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if abandon_count < 0:
        raise ValueError("abandon_count must be non-negative")
    if abandon_count > total_count:
        raise ValueError("abandon_count cannot exceed total_count")
    if abandon_count == 0:
        return float("-inf")
    return math.log(abandon_count / total_count)

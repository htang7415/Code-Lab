from __future__ import annotations

import math


def log_shed_rate(shed_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if shed_count < 0:
        raise ValueError("shed_count must be non-negative")
    if shed_count > total_count:
        raise ValueError("shed_count cannot exceed total_count")
    if shed_count == 0:
        return float("-inf")
    return math.log(shed_count / total_count)

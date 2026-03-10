from __future__ import annotations

import math


def log_escape_rate(escape_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if escape_count < 0:
        raise ValueError("escape_count must be non-negative")
    if escape_count > total_count:
        raise ValueError("escape_count cannot exceed total_count")
    if escape_count == 0:
        return float("-inf")
    return math.log(escape_count / total_count)

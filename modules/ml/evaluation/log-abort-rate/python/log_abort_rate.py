from __future__ import annotations

import math


def log_abort_rate(abort_count: int, total_count: int) -> float:
    if total_count <= 0:
        raise ValueError("total_count must be positive")
    if abort_count < 0:
        raise ValueError("abort_count must be non-negative")
    if abort_count > total_count:
        raise ValueError("abort_count cannot exceed total_count")
    if abort_count == 0:
        return float("-inf")
    return math.log(abort_count / total_count)

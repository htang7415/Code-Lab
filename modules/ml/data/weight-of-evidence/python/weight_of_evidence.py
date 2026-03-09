from __future__ import annotations

import math


def weight_of_evidence(
    positive_count: int,
    negative_count: int,
    total_positive: int,
    total_negative: int,
    smoothing: float = 0.5,
) -> float:
    counts = [positive_count, negative_count, total_positive, total_negative]
    if any(count < 0 for count in counts):
        raise ValueError("counts must be non-negative")
    if total_positive <= 0 or total_negative <= 0:
        raise ValueError("total_positive and total_negative must be positive")
    if positive_count > total_positive or negative_count > total_negative:
        raise ValueError("category counts cannot exceed class totals")
    if smoothing < 0.0:
        raise ValueError("smoothing must be non-negative")

    positive_rate = (positive_count + smoothing) / (total_positive + 2.0 * smoothing)
    negative_rate = (negative_count + smoothing) / (total_negative + 2.0 * smoothing)
    return math.log(positive_rate / negative_rate)

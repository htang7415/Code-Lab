from __future__ import annotations

import math


def overflow_cutoff_tail_variance(
    lengths: list[int],
    max_length: int,
    cutoff: int,
    quantile: float = 0.9,
) -> float:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if cutoff < 0:
        raise ValueError("cutoff must be non-negative")
    if not 0.0 <= quantile <= 1.0:
        raise ValueError("quantile must satisfy 0 <= quantile <= 1")
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    qualifying_overflow = sorted(
        max(0, length - max_length)
        for length in lengths
        if max(0, length - max_length) >= cutoff
    )
    if not qualifying_overflow:
        return 0.0
    if len(qualifying_overflow) == 1:
        return 0.0

    position = (len(qualifying_overflow) - 1) * quantile
    lower_index = math.floor(position)
    upper_index = math.ceil(position)
    if lower_index == upper_index:
        threshold = float(qualifying_overflow[lower_index])
    else:
        weight = position - lower_index
        threshold = qualifying_overflow[lower_index] * (1.0 - weight) + qualifying_overflow[upper_index] * weight

    tail = [value for value in qualifying_overflow if value >= threshold]
    if len(tail) < 2:
        return 0.0

    mean_tail = sum(tail) / len(tail)
    return sum((value - mean_tail) ** 2 for value in tail) / len(tail)

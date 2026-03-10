from __future__ import annotations

import math


def overflow_cutoff_skew(lengths: list[int], max_length: int, cutoff: int) -> float:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if cutoff < 0:
        raise ValueError("cutoff must be non-negative")
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    qualifying_overflow = [max(0, length - max_length) for length in lengths if max(0, length - max_length) >= cutoff]
    if len(qualifying_overflow) < 3:
        return 0.0

    mean_overflow = sum(qualifying_overflow) / len(qualifying_overflow)
    variance = sum((overflow - mean_overflow) ** 2 for overflow in qualifying_overflow) / len(qualifying_overflow)
    if variance == 0.0:
        return 0.0

    std_overflow = math.sqrt(variance)
    third_moment = sum((overflow - mean_overflow) ** 3 for overflow in qualifying_overflow) / len(qualifying_overflow)
    return third_moment / (std_overflow ** 3)

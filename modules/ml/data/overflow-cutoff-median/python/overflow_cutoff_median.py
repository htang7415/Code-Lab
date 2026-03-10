from __future__ import annotations


def overflow_cutoff_median(lengths: list[int], max_length: int, cutoff: int) -> float:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if cutoff < 0:
        raise ValueError("cutoff must be non-negative")
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    qualifying_overflow = sorted(
        max(0, length - max_length)
        for length in lengths
        if max(0, length - max_length) >= cutoff
    )
    if not qualifying_overflow:
        return 0.0

    midpoint = len(qualifying_overflow) // 2
    if len(qualifying_overflow) % 2 == 1:
        return float(qualifying_overflow[midpoint])
    return (qualifying_overflow[midpoint - 1] + qualifying_overflow[midpoint]) / 2

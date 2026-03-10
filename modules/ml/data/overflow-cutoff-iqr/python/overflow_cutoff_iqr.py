from __future__ import annotations


def _quantile(values: list[int], q: float) -> float:
    position = (len(values) - 1) * q
    lower = int(position)
    upper = min(lower + 1, len(values) - 1)
    weight = position - lower
    return values[lower] * (1.0 - weight) + values[upper] * weight


def overflow_cutoff_iqr(lengths: list[int], max_length: int, cutoff: int) -> float:
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
    if len(qualifying_overflow) < 2:
        return 0.0

    return _quantile(qualifying_overflow, 0.75) - _quantile(qualifying_overflow, 0.25)

from __future__ import annotations


def overflow_cutoff_rate(lengths: list[int], max_length: int, cutoff: int) -> float:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if cutoff < 0:
        raise ValueError("cutoff must be non-negative")
    if not lengths:
        return 0.0
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    count = sum(max(0, length - max_length) >= cutoff for length in lengths)
    return count / len(lengths)

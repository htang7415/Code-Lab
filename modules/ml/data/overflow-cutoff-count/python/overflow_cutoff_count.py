from __future__ import annotations


def overflow_cutoff_count(lengths: list[int], max_length: int, cutoff: int) -> int:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if cutoff < 0:
        raise ValueError("cutoff must be non-negative")
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    return sum(max(0, length - max_length) >= cutoff for length in lengths)

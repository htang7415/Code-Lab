from __future__ import annotations


def overflow_threshold_count(lengths: list[int], max_length: int, threshold: int) -> int:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if threshold < 0:
        raise ValueError("threshold must be non-negative")
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    return sum(max(0, length - max_length) > threshold for length in lengths)

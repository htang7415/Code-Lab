from __future__ import annotations


def overflow_threshold_rate(lengths: list[int], max_length: int, threshold: int) -> tuple[int, float]:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if threshold < 0:
        raise ValueError("threshold must be non-negative")
    if not lengths:
        return 0, 0.0
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    count = sum(max(0, length - max_length) > threshold for length in lengths)
    return count, count / len(lengths)

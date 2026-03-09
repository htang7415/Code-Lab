from __future__ import annotations


def overflow_gini(lengths: list[int], max_length: int) -> float:
    if max_length < 0:
        raise ValueError("max_length must be non-negative")
    if not lengths:
        return 0.0
    if any(length < 0 for length in lengths):
        raise ValueError("lengths must be non-negative")

    overflow = sorted(max(0, length - max_length) for length in lengths)
    total = sum(overflow)
    if total == 0:
        return 0.0

    weighted = 0
    count = len(overflow)
    for index, value in enumerate(overflow, start=1):
        weighted += (2 * index - count - 1) * value
    return weighted / (count * total)

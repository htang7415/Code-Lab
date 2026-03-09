from __future__ import annotations

import math


def _positive_rate(labels: list[int]) -> float:
    if not labels:
        return 0.0
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must contain only 0 or 1")
    return sum(labels) / len(labels)


def log_prevalence_ratio(group_a: list[int], group_b: list[int]) -> float:
    rate_a = _positive_rate(group_a)
    rate_b = _positive_rate(group_b)
    if rate_a == 0.0 and rate_b == 0.0:
        return 0.0
    if rate_b == 0.0:
        return float("inf")
    if rate_a == 0.0:
        return float("-inf")
    return math.log(rate_a / rate_b)

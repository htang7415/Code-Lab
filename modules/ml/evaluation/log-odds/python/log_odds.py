from __future__ import annotations

import math


def log_odds(labels: list[int]) -> float:
    if not labels:
        return 0.0
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must contain only 0 or 1")

    rate = sum(labels) / len(labels)
    if rate == 0.0:
        return float("-inf")
    if rate == 1.0:
        return float("inf")
    return math.log(rate / (1.0 - rate))

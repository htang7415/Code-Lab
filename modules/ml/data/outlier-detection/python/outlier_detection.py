from __future__ import annotations

import math


def z_score_outliers(values: list[float], threshold: float = 3.0) -> list[int]:
    if threshold <= 0.0:
        raise ValueError("threshold must be positive")
    if not values:
        return []

    mean = sum(values) / len(values)
    variance = sum((value - mean) ** 2 for value in values) / len(values)
    if variance == 0.0:
        return []

    std = math.sqrt(variance)
    return [
        index
        for index, value in enumerate(values)
        if abs((value - mean) / std) > threshold
    ]

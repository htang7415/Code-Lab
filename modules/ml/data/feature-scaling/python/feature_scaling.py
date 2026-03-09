from __future__ import annotations

import math


def feature_scale(values: list[float], method: str = "zscore") -> list[float]:
    if not values:
        return []

    if method == "zscore":
        mean = sum(values) / len(values)
        variance = sum((value - mean) ** 2 for value in values) / len(values)
        if variance == 0.0:
            return [0.0 for _ in values]
        std = math.sqrt(variance)
        return [(value - mean) / std for value in values]

    if method == "minmax":
        min_value = min(values)
        max_value = max(values)
        if max_value == min_value:
            return [0.0 for _ in values]
        return [(value - min_value) / (max_value - min_value) for value in values]

    raise ValueError("method must be 'zscore' or 'minmax'")

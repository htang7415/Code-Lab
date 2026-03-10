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


def _quantile(sorted_values: list[float], q: float) -> float:
    position = q * (len(sorted_values) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return sorted_values[lower]
    weight = position - lower
    return sorted_values[lower] * (1.0 - weight) + sorted_values[upper] * weight


def robust_scale(values: list[float]) -> list[float]:
    if not values:
        return []

    sorted_values = sorted(values)
    median = _quantile(sorted_values, 0.5)
    q1 = _quantile(sorted_values, 0.25)
    q3 = _quantile(sorted_values, 0.75)
    iqr = q3 - q1
    if iqr == 0.0:
        return [0.0 for _ in values]
    return [(value - median) / iqr for value in values]


def clip_features(values: list[float], min_value: float, max_value: float) -> list[float]:
    if min_value > max_value:
        raise ValueError("min_value must be less than or equal to max_value")
    return [min(max(value, min_value), max_value) for value in values]

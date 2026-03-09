from __future__ import annotations

import math


def _quantile(sorted_values: list[float], q: float) -> float:
    position = q * (len(sorted_values) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return sorted_values[lower]
    weight = position - lower
    return sorted_values[lower] * (1.0 - weight) + sorted_values[upper] * weight


def bootstrap_percentile_interval(
    bootstrap_statistics: list[float],
    alpha: float = 0.05,
) -> tuple[float, float]:
    if len(bootstrap_statistics) < 2:
        raise ValueError("bootstrap_statistics must contain at least two values")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must satisfy 0 < alpha < 1")

    sorted_values = sorted(bootstrap_statistics)
    lower = _quantile(sorted_values, alpha / 2.0)
    upper = _quantile(sorted_values, 1.0 - alpha / 2.0)
    return lower, upper

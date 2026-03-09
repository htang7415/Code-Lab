from __future__ import annotations

import math


def mean_confidence_interval(
    samples: list[float],
    z: float = 1.96,
) -> tuple[float, float]:
    if len(samples) < 2:
        raise ValueError("samples must contain at least two values")
    if z <= 0.0:
        raise ValueError("z must be positive")

    mean = sum(samples) / len(samples)
    variance = sum((sample - mean) ** 2 for sample in samples) / (len(samples) - 1)
    margin = z * math.sqrt(variance) / math.sqrt(len(samples))
    return mean - margin, mean + margin

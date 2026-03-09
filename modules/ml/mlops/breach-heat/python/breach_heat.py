from __future__ import annotations


def breach_heat(observations: list[float], capacity: float) -> float:
    if capacity <= 0.0:
        raise ValueError("capacity must be positive")
    if any(observation < 0.0 for observation in observations):
        raise ValueError("observations must be non-negative")

    total = 0.0
    for observation in observations:
        if observation > capacity:
            excess_ratio = (observation - capacity) / capacity
            total += excess_ratio * excess_ratio
    return total

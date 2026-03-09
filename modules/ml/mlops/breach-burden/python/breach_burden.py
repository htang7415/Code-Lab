from __future__ import annotations


def breach_burden(observations: list[float], capacity: float) -> float:
    if capacity <= 0.0:
        raise ValueError("capacity must be positive")
    if any(observation < 0.0 for observation in observations):
        raise ValueError("observations must be non-negative")

    return sum(
        max(0.0, (observation - capacity) / capacity)
        for observation in observations
    )

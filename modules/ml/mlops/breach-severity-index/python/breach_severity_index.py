from __future__ import annotations


def breach_severity_index(observations: list[float], capacity: float) -> float:
    if capacity <= 0.0:
        raise ValueError("capacity must be positive")
    if not observations:
        return 0.0
    if any(observation < 0.0 for observation in observations):
        raise ValueError("observations must be non-negative")

    breached = [observation for observation in observations if observation > capacity]
    if not breached:
        return 0.0

    breach_rate = len(breached) / len(observations)
    mean_excess_ratio = sum((observation - capacity) / capacity for observation in breached) / len(breached)
    return breach_rate * (1.0 + mean_excess_ratio)

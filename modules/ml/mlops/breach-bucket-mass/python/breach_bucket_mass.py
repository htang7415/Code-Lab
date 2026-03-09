from __future__ import annotations


def breach_bucket_mass(observations: list[float], capacity: float, cutoffs: list[float]) -> list[float]:
    if capacity <= 0.0:
        raise ValueError("capacity must be positive")
    if any(observation < 0.0 for observation in observations):
        raise ValueError("observations must be non-negative")
    if any(cutoff < 0.0 for cutoff in cutoffs):
        raise ValueError("cutoffs must be non-negative")
    if any(left > right for left, right in zip(cutoffs, cutoffs[1:])):
        raise ValueError("cutoffs must be sorted")

    mass = [0.0] * (len(cutoffs) + 1)
    total_mass = 0.0
    for observation in observations:
        if observation <= capacity:
            continue

        excess_ratio = (observation - capacity) / capacity
        total_mass += excess_ratio
        bucket_index = len(cutoffs)
        for index, cutoff in enumerate(cutoffs):
            if excess_ratio <= cutoff:
                bucket_index = index
                break
        mass[bucket_index] += excess_ratio

    if total_mass == 0.0:
        return [0.0] * len(mass)
    return [bucket_mass / total_mass for bucket_mass in mass]

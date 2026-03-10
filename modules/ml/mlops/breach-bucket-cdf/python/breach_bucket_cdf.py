from __future__ import annotations


def breach_bucket_cdf(observations: list[float], capacity: float, cutoffs: list[float]) -> list[float]:
    if capacity <= 0.0:
        raise ValueError("capacity must be positive")
    if any(observation < 0.0 for observation in observations):
        raise ValueError("observations must be non-negative")
    if any(cutoff < 0.0 for cutoff in cutoffs):
        raise ValueError("cutoffs must be non-negative")
    if any(left > right for left, right in zip(cutoffs, cutoffs[1:])):
        raise ValueError("cutoffs must be sorted")

    counts = [0] * (len(cutoffs) + 1)
    breached_count = 0
    for observation in observations:
        if observation <= capacity:
            continue

        breached_count += 1
        excess_ratio = (observation - capacity) / capacity
        bucket_index = len(cutoffs)
        for index, cutoff in enumerate(cutoffs):
            if excess_ratio <= cutoff:
                bucket_index = index
                break
        counts[bucket_index] += 1

    if breached_count == 0:
        return [0.0] * len(counts)

    cumulative = []
    running_total = 0
    for count in counts:
        running_total += count
        cumulative.append(running_total / breached_count)
    return cumulative

from __future__ import annotations


def breach_bucket_turning_point(
    observations: list[float],
    capacity: float,
    cutoffs: list[float],
) -> int:
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

    if breached_count == 0 or len(counts) < 3:
        return -1

    shares = [count / breached_count for count in counts]
    best_index = -1
    best_peak = 0.0
    for index in range(1, len(shares) - 1):
        if shares[index] >= shares[index - 1] and shares[index] > shares[index + 1]:
            peak_strength = shares[index] - shares[index + 1]
            if peak_strength > best_peak:
                best_peak = peak_strength
                best_index = index
    return best_index

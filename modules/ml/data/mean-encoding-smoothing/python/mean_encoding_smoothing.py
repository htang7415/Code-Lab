from __future__ import annotations


def smoothed_mean_encoding_map(categories: list[str], targets: list[float], smoothing: float) -> dict[str, float]:
    if len(categories) != len(targets):
        raise ValueError("categories and targets must have the same length")
    if smoothing < 0.0:
        raise ValueError("smoothing must be non-negative")
    if not categories:
        return {}

    global_mean = sum(targets) / len(targets)
    sums: dict[str, float] = {}
    counts: dict[str, int] = {}

    for category, target in zip(categories, targets):
        sums[category] = sums.get(category, 0.0) + target
        counts[category] = counts.get(category, 0) + 1

    return {
        category: (sums[category] + smoothing * global_mean) / (counts[category] + smoothing)
        for category in sums
    }

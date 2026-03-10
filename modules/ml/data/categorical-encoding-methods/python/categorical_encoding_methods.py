from __future__ import annotations

import math


def frequency_encoding_map(categories: list[str]) -> dict[str, float]:
    if not categories:
        return {}

    counts: dict[str, int] = {}
    for category in categories:
        counts[category] = counts.get(category, 0) + 1

    total = len(categories)
    return {category: count / total for category, count in counts.items()}


def target_encoding_map(categories: list[str], targets: list[float]) -> dict[str, float]:
    if len(categories) != len(targets):
        raise ValueError("categories and targets must have the same length")
    if not categories:
        return {}

    sums: dict[str, float] = {}
    counts: dict[str, int] = {}
    for category, target in zip(categories, targets):
        sums[category] = sums.get(category, 0.0) + target
        counts[category] = counts.get(category, 0) + 1

    return {category: sums[category] / counts[category] for category in sums}


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


def weight_of_evidence(
    positive_count: int,
    negative_count: int,
    total_positive: int,
    total_negative: int,
    smoothing: float = 0.5,
) -> float:
    counts = [positive_count, negative_count, total_positive, total_negative]
    if any(count < 0 for count in counts):
        raise ValueError("counts must be non-negative")
    if total_positive <= 0 or total_negative <= 0:
        raise ValueError("total_positive and total_negative must be positive")
    if positive_count > total_positive or negative_count > total_negative:
        raise ValueError("category counts cannot exceed class totals")
    if smoothing < 0.0:
        raise ValueError("smoothing must be non-negative")

    positive_rate = (positive_count + smoothing) / (total_positive + 2.0 * smoothing)
    negative_rate = (negative_count + smoothing) / (total_negative + 2.0 * smoothing)
    return math.log(positive_rate / negative_rate)


def group_rare_categories(categories: list[str], min_count: int, other_label: str = "__OTHER__") -> list[str]:
    if min_count <= 0:
        raise ValueError("min_count must be positive")

    counts: dict[str, int] = {}
    for category in categories:
        counts[category] = counts.get(category, 0) + 1

    return [category if counts[category] >= min_count else other_label for category in categories]

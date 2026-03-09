from __future__ import annotations


def group_rare_categories(categories: list[str], min_count: int, other_label: str = "__OTHER__") -> list[str]:
    if min_count <= 0:
        raise ValueError("min_count must be positive")

    counts: dict[str, int] = {}
    for category in categories:
        counts[category] = counts.get(category, 0) + 1

    return [category if counts[category] >= min_count else other_label for category in categories]

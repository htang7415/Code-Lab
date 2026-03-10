from __future__ import annotations


def global_average_pool(feature_map: list[list[float]]) -> float:
    if not feature_map or not feature_map[0]:
        raise ValueError("feature_map must be non-empty")

    total = 0.0
    count = 0
    width = len(feature_map[0])
    for row in feature_map:
        if len(row) != width:
            raise ValueError("feature_map rows must have equal length")
        total += sum(row)
        count += len(row)
    return total / count

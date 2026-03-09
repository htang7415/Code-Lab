from __future__ import annotations


def mean_impute(table: list[list[float | None]]) -> list[list[float]]:
    if not table:
        return []

    width = len(table[0])
    for row in table:
        if len(row) != width:
            raise ValueError("all rows must have the same length")

    sums = [0.0] * width
    counts = [0] * width
    for row in table:
        for j, value in enumerate(row):
            if value is None:
                continue
            sums[j] += value
            counts[j] += 1

    means = [sums[j] / counts[j] if counts[j] else 0.0 for j in range(width)]

    filled: list[list[float]] = []
    for row in table:
        filled.append([means[j] if value is None else value for j, value in enumerate(row)])
    return filled

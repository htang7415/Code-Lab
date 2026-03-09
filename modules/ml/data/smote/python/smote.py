from __future__ import annotations


def smote_samples(
    minority_points: list[list[float]],
    neighbor_pairs: list[tuple[int, int]],
    gaps: list[float],
) -> list[list[float]]:
    if len(neighbor_pairs) != len(gaps):
        raise ValueError("neighbor_pairs and gaps must have the same length")

    samples: list[list[float]] = []
    for (i, j), gap in zip(neighbor_pairs, gaps):
        if not 0.0 <= gap <= 1.0:
            raise ValueError("gap values must be between 0 and 1")
        point = minority_points[i]
        neighbor = minority_points[j]
        if len(point) != len(neighbor):
            raise ValueError("points in a pair must have the same dimension")
        samples.append([
            value + gap * (other - value) for value, other in zip(point, neighbor)
        ])
    return samples

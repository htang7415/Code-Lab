from __future__ import annotations


def tsne_point_gradient(
    point: list[float],
    other_points: list[list[float]],
    affinities: list[float],
) -> list[float]:
    if len(other_points) != len(affinities):
        raise ValueError("other_points and affinities must have the same length")
    if any(len(other) != len(point) for other in other_points):
        raise ValueError("other_points must match the point dimension")
    if any(affinity < 0.0 for affinity in affinities):
        raise ValueError("affinities must be non-negative")
    if not other_points:
        return [0.0] * len(point)

    affinity_sum = sum(affinities)
    if affinity_sum <= 0.0:
        raise ValueError("affinities must sum to a positive value")
    normalized_affinities = [affinity / affinity_sum for affinity in affinities]

    numerators = []
    for other in other_points:
        squared_distance = sum((a - b) ** 2 for a, b in zip(point, other))
        numerators.append(1.0 / (1.0 + squared_distance))

    q_sum = sum(numerators)
    q_values = [numerator / q_sum for numerator in numerators]

    gradient = [0.0] * len(point)
    for p_ij, q_ij, numerator, other in zip(
        normalized_affinities, q_values, numerators, other_points
    ):
        coefficient = 4.0 * (p_ij - q_ij) * numerator
        for dimension in range(len(point)):
            gradient[dimension] += coefficient * (point[dimension] - other[dimension])
    return gradient

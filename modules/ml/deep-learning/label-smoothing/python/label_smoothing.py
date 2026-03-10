from __future__ import annotations

import math


def label_smoothed_cross_entropy(
    probabilities: list[float],
    target_index: int,
    smoothing: float,
) -> float:
    if not probabilities:
        raise ValueError("probabilities must be non-empty")
    if any(probability <= 0.0 or probability > 1.0 for probability in probabilities):
        raise ValueError("probabilities must lie in (0, 1]")
    if not math.isclose(sum(probabilities), 1.0, rel_tol=1e-9, abs_tol=1e-9):
        raise ValueError("probabilities must sum to 1")
    if not 0.0 <= smoothing < 1.0:
        raise ValueError("smoothing must satisfy 0 <= smoothing < 1")
    if not 0 <= target_index < len(probabilities):
        raise ValueError("target_index must be in range")
    if len(probabilities) == 1:
        return -math.log(probabilities[0])

    off_target = smoothing / (len(probabilities) - 1)
    loss = 0.0
    for index, probability in enumerate(probabilities):
        target_probability = 1.0 - smoothing if index == target_index else off_target
        loss -= target_probability * math.log(probability)
    return loss

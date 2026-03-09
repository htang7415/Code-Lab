from __future__ import annotations

import math


def log_loss(labels: list[int], probabilities: list[float], eps: float = 1.0e-15) -> float:
    if len(labels) != len(probabilities):
        raise ValueError("labels and probabilities must have the same length")
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must be binary")
    if any(probability < 0.0 or probability > 1.0 for probability in probabilities):
        raise ValueError("probabilities must satisfy 0 <= p <= 1")
    if eps <= 0.0:
        raise ValueError("eps must be positive")
    if not labels:
        return 0.0

    total = 0.0
    for label, probability in zip(labels, probabilities):
        clipped = min(max(probability, eps), 1.0 - eps)
        total += label * math.log(clipped) + (1 - label) * math.log(1.0 - clipped)
    return -total / len(labels)

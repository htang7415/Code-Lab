import math


def update_weights(weights: list[float], errors: list[int], alpha: float) -> list[float]:
    updated = [w * math.exp(alpha * e) for w, e in zip(weights, errors)]
    s = sum(updated)
    return [w / s for w in updated]

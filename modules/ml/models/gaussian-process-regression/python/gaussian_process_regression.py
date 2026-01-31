import math


def rbf_kernel(x: list[float], y: list[float], length_scale: float) -> float:
    dist2 = sum((a - b) ** 2 for a, b in zip(x, y))
    return math.exp(-dist2 / (2 * length_scale ** 2))

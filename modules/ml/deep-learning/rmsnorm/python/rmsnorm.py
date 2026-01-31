import math


def rmsnorm(x: list[float], eps: float = 1e-5) -> list[float]:
    rms = math.sqrt(sum(v * v for v in x) / len(x) + eps)
    return [v / rms for v in x]

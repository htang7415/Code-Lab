import math


def instancenorm(x: list[float], eps: float = 1e-5) -> list[float]:
    mean = sum(x) / len(x)
    var = sum((v - mean) ** 2 for v in x) / len(x)
    return [(v - mean) / math.sqrt(var + eps) for v in x]

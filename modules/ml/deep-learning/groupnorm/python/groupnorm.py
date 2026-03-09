import math


def groupnorm(x: list[float], groups: int, eps: float = 1e-5) -> list[float]:
    if groups <= 0:
        raise ValueError("groups must be positive")
    size = len(x)
    if size == 0:
        raise ValueError("x must be non-empty")
    if size % groups != 0:
        raise ValueError("len(x) must be divisible by groups")

    group_size = size // groups
    out = []
    for g in range(groups):
        chunk = x[g * group_size : (g + 1) * group_size]
        mean = sum(chunk) / len(chunk)
        var = sum((v - mean) ** 2 for v in chunk) / len(chunk)
        out.extend([(v - mean) / math.sqrt(var + eps) for v in chunk])
    return out

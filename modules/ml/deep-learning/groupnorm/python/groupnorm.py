import math


def groupnorm(x: list[float], groups: int, eps: float = 1e-5) -> list[float]:
    size = len(x)
    group_size = size // groups
    out = []
    for g in range(groups):
        chunk = x[g * group_size : (g + 1) * group_size]
        mean = sum(chunk) / len(chunk)
        var = sum((v - mean) ** 2 for v in chunk) / len(chunk)
        out.extend([(v - mean) / math.sqrt(var + eps) for v in chunk])
    return out

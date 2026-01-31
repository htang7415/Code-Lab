import math


def normalize(values: list[float]) -> list[float]:
    mean = sum(values) / len(values)
    var = sum((v - mean) ** 2 for v in values) / len(values)
    std = math.sqrt(var) if var > 0 else 1.0
    return [(v - mean) / std for v in values]

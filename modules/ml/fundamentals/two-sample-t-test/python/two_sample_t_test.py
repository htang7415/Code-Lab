import math


def t_stat(x: list[float], y: list[float]) -> float:
    m1 = sum(x) / len(x)
    m2 = sum(y) / len(y)
    v1 = sum((v - m1) ** 2 for v in x) / (len(x) - 1)
    v2 = sum((v - m2) ** 2 for v in y) / (len(y) - 1)
    return (m1 - m2) / math.sqrt(v1 / len(x) + v2 / len(y))

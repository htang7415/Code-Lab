import math


def t_stat(x: list[float], y: list[float]) -> float:
    m1 = sum(x) / len(x)
    m2 = sum(y) / len(y)
    v1 = sum((v - m1) ** 2 for v in x) / (len(x) - 1)
    v2 = sum((v - m2) ** 2 for v in y) / (len(y) - 1)
    denom = math.sqrt(v1 / len(x) + v2 / len(y))
    if denom == 0:
        if m1 == m2:
            return 0.0
        return float("-inf") if m1 < m2 else float("inf")
    return (m1 - m2) / denom

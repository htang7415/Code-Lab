import math


def psi(expected: list[float], actual: list[float]) -> float:
    total = 0.0
    for e, a in zip(expected, actual):
        if e > 0 and a > 0:
            total += (a - e) * math.log(a / e)
    return total

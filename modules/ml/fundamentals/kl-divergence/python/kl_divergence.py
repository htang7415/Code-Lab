import math


def kl(p: list[float], q: list[float]) -> float:
    total = 0.0
    for pi, qi in zip(p, q):
        if pi > 0 and qi > 0:
            total += pi * math.log(pi / qi)
    return total

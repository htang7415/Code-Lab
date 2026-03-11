import math


def kl(p: list[float], q: list[float]) -> float:
    if len(p) != len(q):
        raise ValueError("p and q must have the same length")

    total = 0.0
    for pi, qi in zip(p, q):
        if pi < 0.0 or qi < 0.0:
            raise ValueError("p and q must be non-negative")
        if pi == 0.0:
            continue
        if qi == 0.0:
            return float("inf")
        total += pi * math.log(pi / qi)
    return total

import math


def kl_penalty(p: list[float], q: list[float], beta: float) -> float:
    kl = 0.0
    for pi, qi in zip(p, q):
        if pi > 0 and qi > 0:
            kl += pi * math.log(pi / qi)
    return beta * kl

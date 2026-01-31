import math


def js(p: list[float], q: list[float]) -> float:
    m = [(pi + qi) / 2 for pi, qi in zip(p, q)]
    def kl(a, b):
        return sum(ai * math.log(ai / bi) for ai, bi in zip(a, b) if ai > 0 and bi > 0)
    return 0.5 * kl(p, m) + 0.5 * kl(q, m)

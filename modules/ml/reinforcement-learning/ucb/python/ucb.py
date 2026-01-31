import math


def ucb_score(q: float, t: int, n: int, c: float = 1.0) -> float:
    return q + c * math.sqrt(math.log(t) / n)

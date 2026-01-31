import math


def bernoulli_log_likelihood(x: list[int], prob: list[float]) -> float:
    ll = 0.0
    for xi, p in zip(x, prob):
        ll += xi * math.log(p) + (1 - xi) * math.log(1 - p)
    return ll

import math


def gaussian_log_likelihood(x: list[float], mean: list[float], var: list[float]) -> float:
    ll = 0.0
    for xi, mu, v in zip(x, mean, var):
        ll += -0.5 * (math.log(2 * math.pi * v) + ((xi - mu) ** 2) / v)
    return ll

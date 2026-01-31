import math


def exp_decay(lr: float, k: float, t: float) -> float:
    return lr * math.exp(-k * t)

import math


def cosine_decay(lr: float, t: int, t_max: int) -> float:
    return lr * 0.5 * (1 + math.cos(math.pi * t / t_max))

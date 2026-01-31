import math


def step_decay(lr: float, step: int, gamma: float, t: int) -> float:
    return lr * (gamma ** (t // step))

import math


def focal_loss(p: float, gamma: float = 2.0) -> float:
    return -((1 - p) ** gamma) * math.log(p)

import math


def gan_loss(d_real: float, d_fake: float) -> float:
    return -math.log(d_real) - math.log(1 - d_fake)

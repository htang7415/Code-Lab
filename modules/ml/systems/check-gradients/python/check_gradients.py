import math


def gradients_ok(grads: list[float]) -> bool:
    if any(math.isnan(g) for g in grads):
        return False
    return any(abs(g) > 0 for g in grads)

import math


def adam_step(w: float, grad: float, m: float, v: float, lr: float, beta1: float, beta2: float, eps: float) -> tuple[float, float, float]:
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1 - beta2) * (grad ** 2)
    w = w - lr * m / (math.sqrt(v) + eps)
    return w, m, v

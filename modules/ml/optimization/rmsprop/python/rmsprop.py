import math


def rmsprop_step(w: float, grad: float, v: float, lr: float, beta: float, eps: float) -> tuple[float, float]:
    v = beta * v + (1 - beta) * (grad ** 2)
    w = w - lr * grad / (math.sqrt(v) + eps)
    return w, v

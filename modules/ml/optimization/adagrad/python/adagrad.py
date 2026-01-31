import math


def adagrad_step(w: float, grad: float, g2: float, lr: float, eps: float) -> tuple[float, float]:
    g2 = g2 + grad ** 2
    w = w - lr * grad / (math.sqrt(g2) + eps)
    return w, g2

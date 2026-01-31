def gd_step(x: float, grad: float, lr: float) -> float:
    return x - lr * grad

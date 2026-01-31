def sgd_step(w: float, grad: float, lr: float) -> float:
    return w - lr * grad

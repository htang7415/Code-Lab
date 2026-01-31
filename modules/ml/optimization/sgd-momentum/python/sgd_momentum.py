def momentum_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
    v = mu * v + grad
    w = w - lr * v
    return w, v

def weight_decay_step(w: float, grad: float, lr: float, lam: float) -> float:
    return w - lr * (grad + lam * w)

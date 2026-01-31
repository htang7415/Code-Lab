def nesterov_step(w: float, grad: float, v: float, lr: float, mu: float) -> tuple[float, float]:
    v_new = mu * v + grad
    w_new = w - lr * (mu * v_new + grad)
    return w_new, v_new

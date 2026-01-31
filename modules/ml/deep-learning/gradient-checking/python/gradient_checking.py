def grad_check(f, x: float, eps: float = 1e-5) -> float:
    return (f(x + eps) - f(x - eps)) / (2 * eps)

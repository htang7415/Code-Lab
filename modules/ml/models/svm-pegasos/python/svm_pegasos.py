def pegasos_step(w: list[float], x: list[float], y: int, lr: float, lam: float) -> list[float]:
    dot = sum(wi * xi for wi, xi in zip(w, x))
    scale = 1 - lr * lam
    w = [wi * scale for wi in w]
    if y * dot < 1:
        w = [wi + lr * y * xi for wi, xi in zip(w, x)]
    return w

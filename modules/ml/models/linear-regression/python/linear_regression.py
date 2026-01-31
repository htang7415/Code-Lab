def predict(x: list[float], w: list[float], b: float) -> float:
    return sum(wi * xi for wi, xi in zip(w, x)) + b

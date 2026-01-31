import math


def predict_proba(x: list[float], w: list[float], b: float) -> float:
    z = sum(wi * xi for wi, xi in zip(w, x)) + b
    return 1 / (1 + math.exp(-z))

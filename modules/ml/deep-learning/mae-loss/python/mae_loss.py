def mae(y: list[float], y_hat: list[float]) -> float:
    return sum(abs(a - b) for a, b in zip(y, y_hat)) / len(y)

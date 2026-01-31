def mse(y: list[float], y_hat: list[float]) -> float:
    return sum((a - b) ** 2 for a, b in zip(y, y_hat)) / len(y)

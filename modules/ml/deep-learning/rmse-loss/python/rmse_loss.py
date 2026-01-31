import math


def rmse(y: list[float], y_hat: list[float]) -> float:
    mse = sum((a - b) ** 2 for a, b in zip(y, y_hat)) / len(y)
    return math.sqrt(mse)

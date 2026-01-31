def mae_mse(y: list[float], y_hat: list[float]) -> tuple[float, float]:
    mae = sum(abs(a - b) for a, b in zip(y, y_hat)) / len(y)
    mse = sum((a - b) ** 2 for a, b in zip(y, y_hat)) / len(y)
    return mae, mse

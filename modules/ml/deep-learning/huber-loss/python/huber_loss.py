def huber(y: float, y_hat: float, delta: float = 1.0) -> float:
    e = y - y_hat
    if abs(e) <= delta:
        return 0.5 * e * e
    return delta * (abs(e) - 0.5 * delta)

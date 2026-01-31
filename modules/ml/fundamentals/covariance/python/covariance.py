def covariance(x: list[float], y: list[float]) -> float:
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)
    return sum((a - mean_x) * (b - mean_y) for a, b in zip(x, y)) / len(x)

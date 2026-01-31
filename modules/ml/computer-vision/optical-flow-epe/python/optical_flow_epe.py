def epe(pred: tuple[float, float], target: tuple[float, float]) -> float:
    return ((pred[0] - target[0]) ** 2 + (pred[1] - target[1]) ** 2) ** 0.5

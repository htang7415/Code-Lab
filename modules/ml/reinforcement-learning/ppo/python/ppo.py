def clip_ratio(ratio: float, eps: float) -> float:
    return max(1 - eps, min(1 + eps, ratio))

def l2_penalty(weights: list[float], lam: float) -> float:
    return lam * sum(w * w for w in weights)

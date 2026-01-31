def l1_penalty(weights: list[float], lam: float) -> float:
    return lam * sum(abs(w) for w in weights)

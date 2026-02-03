def l1_penalty(weights: list[float], lam: float) -> float:
    return round(lam * sum(abs(w) for w in weights), 10)

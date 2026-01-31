def r2_score(y: list[float], y_hat: list[float]) -> float:
    mean = sum(y) / len(y)
    ss_res = sum((a - b) ** 2 for a, b in zip(y, y_hat))
    ss_tot = sum((a - mean) ** 2 for a in y)
    return 1 - ss_res / ss_tot if ss_tot > 0 else 0.0

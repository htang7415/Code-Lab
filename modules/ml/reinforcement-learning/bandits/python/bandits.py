def update_value(q: float, n: int, reward: float) -> float:
    return q + (reward - q) / n

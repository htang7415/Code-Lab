def discounted_return(rewards: list[float], gamma: float) -> float:
    total = 0.0
    for i, r in enumerate(rewards):
        total += (gamma ** i) * r
    return total

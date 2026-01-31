def q_update(q: float, reward: float, next_max: float, alpha: float, gamma: float) -> float:
    return q + alpha * (reward + gamma * next_max - q)

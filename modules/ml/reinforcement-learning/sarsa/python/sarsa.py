def sarsa_update(q: float, reward: float, next_q: float, alpha: float, gamma: float) -> float:
    return q + alpha * (reward + gamma * next_q - q)

def reinforce_update(grad_logp: float, reward: float, lr: float) -> float:
    return lr * reward * grad_logp

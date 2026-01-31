import math


def dpo_loss(delta_logp: float, delta_logp_ref: float, beta: float = 0.1) -> float:
    diff = beta * (delta_logp - delta_logp_ref)
    return -math.log(1 / (1 + math.exp(-diff)))

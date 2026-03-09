from __future__ import annotations


def n_step_return(rewards: list[float], gamma: float, bootstrap_value: float = 0.0) -> float:
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")

    total = 0.0
    discount = 1.0
    for reward in rewards:
        total += discount * reward
        discount *= gamma
    total += discount * bootstrap_value
    return total

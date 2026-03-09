from __future__ import annotations


def n_step_td_target(
    rewards: list[float],
    bootstrap_value: float,
    gamma: float,
) -> float:
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")

    target = 0.0
    for step, reward in enumerate(rewards):
        target += (gamma ** step) * reward
    target += (gamma ** len(rewards)) * bootstrap_value
    return target

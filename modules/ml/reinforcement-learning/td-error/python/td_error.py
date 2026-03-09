from __future__ import annotations


def td_error(reward: float, gamma: float, next_value: float, value: float) -> float:
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")
    return reward + gamma * next_value - value

from __future__ import annotations


def first_visit_returns(
    states: list[str],
    rewards: list[float],
    gamma: float,
) -> dict[str, float]:
    if len(states) != len(rewards):
        raise ValueError("states and rewards must have the same length")
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")

    returns: dict[str, float] = {}
    discounted_return = 0.0

    for timestep in range(len(states) - 1, -1, -1):
        discounted_return = rewards[timestep] + gamma * discounted_return
        if states[timestep] not in states[:timestep]:
            returns[states[timestep]] = discounted_return

    return returns

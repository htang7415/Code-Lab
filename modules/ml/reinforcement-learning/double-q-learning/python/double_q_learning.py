from __future__ import annotations


def double_q_target(reward: float, gamma: float, selector_values: list[float], evaluator_values: list[float]) -> float:
    if len(selector_values) != len(evaluator_values):
        raise ValueError("selector_values and evaluator_values must have the same length")
    if not selector_values:
        raise ValueError("selector_values and evaluator_values must be non-empty")
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")

    best_action = max(range(len(selector_values)), key=selector_values.__getitem__)
    return reward + gamma * evaluator_values[best_action]

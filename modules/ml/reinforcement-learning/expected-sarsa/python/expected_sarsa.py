from __future__ import annotations


def expected_sarsa_target(
    reward: float,
    gamma: float,
    next_action_probs: list[float],
    next_q_values: list[float],
) -> float:
    if len(next_action_probs) != len(next_q_values):
        raise ValueError("next_action_probs and next_q_values must have the same length")
    if not next_action_probs:
        raise ValueError("next_action_probs and next_q_values must be non-empty")
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")
    if any(probability < 0.0 for probability in next_action_probs):
        raise ValueError("next_action_probs must be non-negative")

    probability_sum = sum(next_action_probs)
    if abs(probability_sum - 1.0) > 1e-9:
        raise ValueError("next_action_probs must sum to 1")

    expected_next_value = sum(probability * q_value for probability, q_value in zip(next_action_probs, next_q_values))
    return reward + gamma * expected_next_value

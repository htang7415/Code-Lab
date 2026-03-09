import pytest

from expected_sarsa import expected_sarsa_target


def test_expected_sarsa_target_uses_policy_weighted_next_value() -> None:
    target = expected_sarsa_target(
        reward=1.0,
        gamma=0.9,
        next_action_probs=[0.25, 0.75],
        next_q_values=[2.0, 4.0],
    )

    assert target == pytest.approx(4.15)


def test_expected_sarsa_target_requires_probabilities_to_sum_to_one() -> None:
    with pytest.raises(ValueError, match="sum to 1"):
        expected_sarsa_target(reward=1.0, gamma=0.9, next_action_probs=[0.2, 0.2], next_q_values=[1.0, 2.0])


def test_expected_sarsa_target_requires_valid_gamma() -> None:
    with pytest.raises(ValueError, match="gamma"):
        expected_sarsa_target(reward=1.0, gamma=1.5, next_action_probs=[1.0], next_q_values=[1.0])

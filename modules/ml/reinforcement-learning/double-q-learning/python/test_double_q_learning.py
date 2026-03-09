import pytest

from double_q_learning import double_q_target


def test_double_q_target_uses_selector_for_argmax_and_evaluator_for_bootstrap() -> None:
    target = double_q_target(
        reward=1.0,
        gamma=0.9,
        selector_values=[2.0, 5.0, 4.0],
        evaluator_values=[10.0, 3.0, 8.0],
    )

    assert target == pytest.approx(3.7)


def test_double_q_target_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        double_q_target(reward=1.0, gamma=0.9, selector_values=[1.0], evaluator_values=[1.0, 2.0])


def test_double_q_target_requires_valid_gamma() -> None:
    with pytest.raises(ValueError, match="gamma"):
        double_q_target(reward=1.0, gamma=1.5, selector_values=[1.0], evaluator_values=[1.0])

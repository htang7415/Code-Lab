import pytest

from n_step_td_prediction import n_step_td_target


def test_n_step_td_target_matches_discounted_rewards_plus_bootstrap() -> None:
    target = n_step_td_target(
        rewards=[1.0, 2.0, 3.0],
        bootstrap_value=4.0,
        gamma=0.5,
    )

    assert target == pytest.approx(3.25)


def test_n_step_td_target_returns_bootstrap_value_for_zero_steps() -> None:
    assert n_step_td_target([], bootstrap_value=7.0, gamma=0.9) == pytest.approx(7.0)


def test_n_step_td_target_requires_valid_discount() -> None:
    with pytest.raises(ValueError, match="gamma"):
        n_step_td_target([1.0], bootstrap_value=0.0, gamma=1.5)

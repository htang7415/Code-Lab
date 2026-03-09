import pytest

from n_step_return import n_step_return


def test_n_step_return_adds_discounted_rewards_and_bootstrap_value() -> None:
    value = n_step_return(rewards=[1.0, 2.0], gamma=0.9, bootstrap_value=10.0)

    assert value == pytest.approx(1.0 + 0.9 * 2.0 + 0.9 * 0.9 * 10.0)


def test_n_step_return_handles_empty_reward_list() -> None:
    value = n_step_return(rewards=[], gamma=0.9, bootstrap_value=5.0)

    assert value == pytest.approx(5.0)


def test_n_step_return_requires_valid_gamma() -> None:
    with pytest.raises(ValueError, match="gamma"):
        n_step_return(rewards=[1.0], gamma=1.2)

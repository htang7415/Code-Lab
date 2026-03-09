import pytest

from td_error import td_error


def test_td_error_computes_bellman_residual() -> None:
    error = td_error(reward=1.0, gamma=0.9, next_value=2.0, value=2.5)

    assert error == pytest.approx(0.3)


def test_td_error_can_be_negative() -> None:
    error = td_error(reward=0.0, gamma=0.9, next_value=1.0, value=2.0)

    assert error == pytest.approx(-1.1)


def test_td_error_requires_valid_gamma() -> None:
    with pytest.raises(ValueError, match="gamma"):
        td_error(reward=1.0, gamma=1.2, next_value=1.0, value=0.0)

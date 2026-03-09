import pytest

from xgboost_objective import split_gain


def test_split_gain_matches_formula():
    value = split_gain(
        left_grad=2.0,
        left_hess=1.0,
        right_grad=-1.0,
        right_hess=1.0,
        lambda_reg=1.0,
        gamma=0.1,
    )
    assert value == pytest.approx(0.9833333333)


def test_split_gain_larger_gamma_reduces_gain():
    small_penalty = split_gain(2.0, 1.0, -1.0, 1.0, 1.0, 0.1)
    large_penalty = split_gain(2.0, 1.0, -1.0, 1.0, 1.0, 0.5)
    assert large_penalty < small_penalty

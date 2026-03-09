import pytest

from surge_pressure import surge_pressure


def test_surge_pressure_weights_larger_breaches_more_heavily() -> None:
    score = surge_pressure([0.8, 1.0, 1.3, 0.9, 1.5], capacity=1.0)

    assert score == pytest.approx((0.0 + 0.0 + 0.09 + 0.0 + 0.25) / 5)


def test_surge_pressure_returns_zero_for_empty_input() -> None:
    assert surge_pressure([], capacity=1.0) == pytest.approx(0.0)


def test_surge_pressure_requires_positive_capacity() -> None:
    with pytest.raises(ValueError, match="positive"):
        surge_pressure([1.0], capacity=0.0)

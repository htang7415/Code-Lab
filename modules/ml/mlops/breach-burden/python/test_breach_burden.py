import pytest

from breach_burden import breach_burden


def test_breach_burden_sums_normalized_excess_above_capacity() -> None:
    burden = breach_burden([0.8, 1.0, 1.3, 0.9, 1.5], capacity=1.0)

    assert burden == pytest.approx(0.8)


def test_breach_burden_returns_zero_when_nothing_breaches() -> None:
    assert breach_burden([0.5, 0.9], capacity=1.0) == pytest.approx(0.0)


def test_breach_burden_requires_positive_capacity() -> None:
    with pytest.raises(ValueError, match="positive"):
        breach_burden([1.0], capacity=0.0)

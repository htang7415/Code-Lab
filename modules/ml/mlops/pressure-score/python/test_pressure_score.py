import pytest

from pressure_score import pressure_score


def test_pressure_score_combines_breach_incidence_and_margin() -> None:
    score = pressure_score([0.8, 1.0, 1.3, 0.9, 1.5], capacity=1.0)

    assert score == pytest.approx((0.0 + 0.0 + 1.3 + 0.0 + 1.5) / 5)


def test_pressure_score_returns_zero_for_empty_input() -> None:
    assert pressure_score([], capacity=1.0) == pytest.approx(0.0)


def test_pressure_score_requires_positive_capacity() -> None:
    with pytest.raises(ValueError, match="positive"):
        pressure_score([1.0], capacity=0.0)

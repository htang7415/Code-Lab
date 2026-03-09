import pytest

from overflow_gini import overflow_gini


def test_overflow_gini_measures_inequality_of_overflow() -> None:
    score = overflow_gini([64, 120, 80, 200], max_length=100)

    assert score == pytest.approx(2.0 / 3.0)


def test_overflow_gini_returns_zero_when_no_lengths_overflow() -> None:
    assert overflow_gini([20, 30, 40], max_length=50) == pytest.approx(0.0)


def test_overflow_gini_requires_non_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_gini([10, -1], max_length=64)

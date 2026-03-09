import pytest

from overflow_threshold_rate import overflow_threshold_rate


def test_overflow_threshold_rate_counts_examples_above_overflow_threshold() -> None:
    count, rate = overflow_threshold_rate([64, 120, 80, 200], max_length=100, threshold=10)

    assert count == 2
    assert rate == pytest.approx(0.5)


def test_overflow_threshold_rate_returns_zero_for_empty_input() -> None:
    assert overflow_threshold_rate([], max_length=64, threshold=5) == (0, 0.0)


def test_overflow_threshold_rate_requires_non_negative_threshold() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_threshold_rate([100], max_length=64, threshold=-1)

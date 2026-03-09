import pytest

from overflow_threshold_count import overflow_threshold_count


def test_overflow_threshold_count_counts_examples_above_overflow_threshold() -> None:
    assert overflow_threshold_count([64, 120, 80, 200], max_length=100, threshold=10) == 2


def test_overflow_threshold_count_returns_zero_for_empty_input() -> None:
    assert overflow_threshold_count([], max_length=64, threshold=5) == 0


def test_overflow_threshold_count_requires_non_negative_threshold() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_threshold_count([100], max_length=64, threshold=-1)

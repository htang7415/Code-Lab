import pytest

from coverage_error import coverage_error


def test_coverage_error_averages_last_relevant_rank() -> None:
    score = coverage_error([[1, 0, 1], [0, 0, 1], [0, 0]])

    assert score == pytest.approx(2.0)


def test_coverage_error_is_zero_for_empty_input() -> None:
    assert coverage_error([]) == pytest.approx(0.0)


def test_coverage_error_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="binary"):
        coverage_error([[0, 2]])

import pytest

from done_fraction import done_fraction


def test_done_fraction_returns_fraction_of_terminal_transitions() -> None:
    assert done_fraction([False, True, False, True]) == pytest.approx(0.5)


def test_done_fraction_returns_zero_for_empty_input() -> None:
    assert done_fraction([]) == pytest.approx(0.0)


def test_done_fraction_is_one_when_all_transitions_are_done() -> None:
    assert done_fraction([True, True]) == pytest.approx(1.0)

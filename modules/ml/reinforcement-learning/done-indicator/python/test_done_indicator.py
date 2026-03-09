import pytest

from done_indicator import done_indicator


def test_done_indicator_returns_one_for_done_transition() -> None:
    assert done_indicator(True) == pytest.approx(1.0)


def test_done_indicator_returns_zero_for_not_done_transition() -> None:
    assert done_indicator(False) == pytest.approx(0.0)


def test_done_indicator_accepts_boolean_values_only_in_usage() -> None:
    assert done_indicator(bool(1)) == pytest.approx(1.0)

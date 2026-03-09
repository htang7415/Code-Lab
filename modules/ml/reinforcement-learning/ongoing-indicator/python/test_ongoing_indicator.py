from __future__ import annotations

from ongoing_indicator import ongoing_indicator


def test_ongoing_indicator_returns_one_for_ongoing_transition() -> None:
    assert ongoing_indicator(False) == 1.0


def test_ongoing_indicator_returns_zero_for_terminal_transition() -> None:
    assert ongoing_indicator(True) == 0.0

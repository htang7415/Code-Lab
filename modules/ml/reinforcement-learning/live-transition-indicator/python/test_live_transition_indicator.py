from __future__ import annotations

from live_transition_indicator import live_transition_indicator


def test_live_transition_indicator_returns_one_for_live_transition() -> None:
    assert live_transition_indicator(False) == 1.0


def test_live_transition_indicator_returns_zero_for_terminal_transition() -> None:
    assert live_transition_indicator(True) == 0.0

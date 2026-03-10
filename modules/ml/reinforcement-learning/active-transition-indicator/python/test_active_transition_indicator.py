from __future__ import annotations

from active_transition_indicator import active_transition_indicator


def test_active_transition_indicator_returns_one_for_active_transition() -> None:
    assert active_transition_indicator(False) == 1.0


def test_active_transition_indicator_returns_zero_for_terminal_transition() -> None:
    assert active_transition_indicator(True) == 0.0

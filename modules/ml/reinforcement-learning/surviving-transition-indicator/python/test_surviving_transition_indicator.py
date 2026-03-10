from __future__ import annotations

from surviving_transition_indicator import surviving_transition_indicator


def test_surviving_transition_indicator_returns_one_for_surviving_transition() -> None:
    assert surviving_transition_indicator(False) == 1.0


def test_surviving_transition_indicator_returns_zero_for_terminal_transition() -> None:
    assert surviving_transition_indicator(True) == 0.0

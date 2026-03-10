from __future__ import annotations

from persistent_transition_indicator import persistent_transition_indicator


def test_persistent_transition_indicator_returns_one_for_persistent_transition() -> None:
    assert persistent_transition_indicator(False) == 1.0


def test_persistent_transition_indicator_returns_zero_for_terminal_transition() -> None:
    assert persistent_transition_indicator(True) == 0.0

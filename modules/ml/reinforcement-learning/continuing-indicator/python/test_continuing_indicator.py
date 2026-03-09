from __future__ import annotations

from continuing_indicator import continuing_indicator


def test_continuing_indicator_returns_one_for_nonterminal_transition() -> None:
    assert continuing_indicator(False) == 1.0


def test_continuing_indicator_returns_zero_for_terminal_transition() -> None:
    assert continuing_indicator(True) == 0.0

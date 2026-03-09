from __future__ import annotations

from nonterminal_indicator import nonterminal_indicator


def test_nonterminal_indicator_returns_one_for_ongoing_transition() -> None:
    assert nonterminal_indicator(False) == 1.0


def test_nonterminal_indicator_returns_zero_for_terminal_transition() -> None:
    assert nonterminal_indicator(True) == 0.0

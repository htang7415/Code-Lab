from __future__ import annotations

from residual_transition_indicator import residual_transition_indicator


def test_residual_transition_indicator_returns_one_for_residual_transition() -> None:
    assert residual_transition_indicator(False) == 1.0


def test_residual_transition_indicator_returns_zero_for_terminal_transition() -> None:
    assert residual_transition_indicator(True) == 0.0

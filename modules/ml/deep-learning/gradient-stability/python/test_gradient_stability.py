from __future__ import annotations

from gradient_stability import gradient_chain, propagate_variance


def test_propagate_variance() -> None:
    assert propagate_variance(1.0, [0.5, 2.0]) == 1.0


def test_gradient_chain() -> None:
    assert gradient_chain([0.5, 0.5]) == 0.25

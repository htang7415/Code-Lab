from __future__ import annotations

import pytest

from breach_heat import breach_heat


def test_breach_heat_accumulates_squared_overload() -> None:
    score = breach_heat([0.8, 1.2, 1.4, 0.9, 1.1], capacity=1.0)

    assert score == pytest.approx(0.21)


def test_breach_heat_returns_zero_when_nothing_breaches() -> None:
    assert breach_heat([0.5, 0.7, 1.0], capacity=1.0) == 0.0


def test_breach_heat_rejects_negative_observations() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        breach_heat([0.8, -0.1], capacity=1.0)

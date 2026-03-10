from __future__ import annotations

import math

import pytest

from log_abandon_rate import log_abandon_rate


def test_log_abandon_rate_returns_log_of_abandon_rate() -> None:
    assert log_abandon_rate(8, 400) == pytest.approx(math.log(0.02))


def test_log_abandon_rate_returns_negative_infinity_for_zero_abandon_rate() -> None:
    assert log_abandon_rate(0, 400) == float("-inf")


def test_log_abandon_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="abandon_count"):
        log_abandon_rate(401, 400)

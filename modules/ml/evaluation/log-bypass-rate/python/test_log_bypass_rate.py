from __future__ import annotations

import math

import pytest

from log_bypass_rate import log_bypass_rate


def test_log_bypass_rate_returns_log_of_bypass_rate() -> None:
    assert log_bypass_rate(16, 800) == pytest.approx(math.log(0.02))


def test_log_bypass_rate_returns_negative_infinity_for_zero_bypass_rate() -> None:
    assert log_bypass_rate(0, 800) == float("-inf")


def test_log_bypass_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="bypass_count"):
        log_bypass_rate(801, 800)

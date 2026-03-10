from __future__ import annotations

import math

import pytest

from log_timeout_rate import log_timeout_rate


def test_log_timeout_rate_returns_log_of_timeout_rate() -> None:
    assert log_timeout_rate(2, 80) == pytest.approx(math.log(0.025))


def test_log_timeout_rate_returns_negative_infinity_for_zero_timeout_rate() -> None:
    assert log_timeout_rate(0, 80) == float("-inf")


def test_log_timeout_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="timeout_count"):
        log_timeout_rate(81, 80)

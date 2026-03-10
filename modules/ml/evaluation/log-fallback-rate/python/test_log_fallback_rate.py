from __future__ import annotations

import math

import pytest

from log_fallback_rate import log_fallback_rate


def test_log_fallback_rate_returns_log_of_fallback_rate() -> None:
    assert log_fallback_rate(10, 500) == pytest.approx(math.log(0.02))


def test_log_fallback_rate_returns_negative_infinity_for_zero_fallback_rate() -> None:
    assert log_fallback_rate(0, 500) == float("-inf")


def test_log_fallback_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="fallback_count"):
        log_fallback_rate(501, 500)

from __future__ import annotations

import math

import pytest

from log_deferral_rate import log_deferral_rate


def test_log_deferral_rate_returns_log_of_deferral_rate() -> None:
    assert log_deferral_rate(6, 300) == pytest.approx(math.log(0.02))


def test_log_deferral_rate_returns_negative_infinity_for_zero_deferral_rate() -> None:
    assert log_deferral_rate(0, 300) == float("-inf")


def test_log_deferral_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="deferral_count"):
        log_deferral_rate(301, 300)

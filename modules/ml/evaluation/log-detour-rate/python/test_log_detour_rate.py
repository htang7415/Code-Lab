from __future__ import annotations

import math

import pytest

from log_detour_rate import log_detour_rate


def test_log_detour_rate_returns_log_of_detour_rate() -> None:
    assert log_detour_rate(14, 700) == pytest.approx(math.log(0.02))


def test_log_detour_rate_returns_negative_infinity_for_zero_detour_rate() -> None:
    assert log_detour_rate(0, 700) == float("-inf")


def test_log_detour_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="detour_count"):
        log_detour_rate(701, 700)

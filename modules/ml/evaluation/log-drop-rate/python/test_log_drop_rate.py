from __future__ import annotations

import math

import pytest

from log_drop_rate import log_drop_rate


def test_log_drop_rate_returns_log_of_drop_rate() -> None:
    assert log_drop_rate(3, 120) == pytest.approx(math.log(0.025))


def test_log_drop_rate_returns_negative_infinity_for_zero_drop_rate() -> None:
    assert log_drop_rate(0, 120) == float("-inf")


def test_log_drop_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="drop_count"):
        log_drop_rate(121, 120)

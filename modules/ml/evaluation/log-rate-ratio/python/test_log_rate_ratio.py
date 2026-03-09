from __future__ import annotations

import math

import pytest

from log_rate_ratio import log_rate_ratio


def test_log_rate_ratio_returns_log_of_rate_ratio() -> None:
    score = log_rate_ratio(30, 100, 10, 100)

    assert score == pytest.approx(math.log(3.0))


def test_log_rate_ratio_returns_negative_infinity_for_zero_rate() -> None:
    assert log_rate_ratio(0, 100, 10, 100) == float("-inf")


def test_log_rate_ratio_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        log_rate_ratio(11, 10, 2, 10)

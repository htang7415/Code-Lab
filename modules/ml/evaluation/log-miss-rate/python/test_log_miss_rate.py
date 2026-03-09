from __future__ import annotations

import math

import pytest

from log_miss_rate import log_miss_rate


def test_log_miss_rate_returns_log_of_miss_rate() -> None:
    score = log_miss_rate(12, 100)

    assert score == pytest.approx(math.log(0.12))


def test_log_miss_rate_returns_negative_infinity_for_zero_miss_rate() -> None:
    assert log_miss_rate(0, 100) == float("-inf")


def test_log_miss_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        log_miss_rate(11, 10)

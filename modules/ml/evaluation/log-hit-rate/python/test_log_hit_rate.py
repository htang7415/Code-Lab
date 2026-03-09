from __future__ import annotations

import math

import pytest

from log_hit_rate import log_hit_rate


def test_log_hit_rate_returns_log_of_hit_rate() -> None:
    score = log_hit_rate(25, 100)

    assert score == pytest.approx(math.log(0.25))


def test_log_hit_rate_returns_negative_infinity_for_zero_hit_rate() -> None:
    assert log_hit_rate(0, 100) == float("-inf")


def test_log_hit_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        log_hit_rate(11, 10)

from __future__ import annotations

import math

import pytest

from log_reject_rate import log_reject_rate


def test_log_reject_rate_returns_log_of_reject_rate() -> None:
    score = log_reject_rate(6, 100)

    assert score == pytest.approx(math.log(0.06))


def test_log_reject_rate_returns_negative_infinity_for_zero_reject_rate() -> None:
    assert log_reject_rate(0, 100) == float("-inf")


def test_log_reject_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        log_reject_rate(11, 10)

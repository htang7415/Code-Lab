from __future__ import annotations

import math

import pytest

from log_error_rate import log_error_rate


def test_log_error_rate_returns_log_of_error_rate() -> None:
    score = log_error_rate(8, 100)

    assert score == pytest.approx(math.log(0.08))


def test_log_error_rate_returns_negative_infinity_for_zero_error_rate() -> None:
    assert log_error_rate(0, 100) == float("-inf")


def test_log_error_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        log_error_rate(11, 10)

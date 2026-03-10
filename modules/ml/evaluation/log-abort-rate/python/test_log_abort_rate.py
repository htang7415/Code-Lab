from __future__ import annotations

import math

import pytest

from log_abort_rate import log_abort_rate


def test_log_abort_rate_returns_log_of_abort_rate() -> None:
    score = log_abort_rate(5, 100)

    assert score == pytest.approx(math.log(0.05))


def test_log_abort_rate_returns_negative_infinity_for_zero_abort_rate() -> None:
    assert log_abort_rate(0, 100) == float("-inf")


def test_log_abort_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        log_abort_rate(11, 10)

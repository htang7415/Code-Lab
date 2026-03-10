from __future__ import annotations

import math

import pytest

from log_defect_rate import log_defect_rate


def test_log_defect_rate_returns_log_of_defect_rate() -> None:
    score = log_defect_rate(4, 100)

    assert score == pytest.approx(math.log(0.04))


def test_log_defect_rate_returns_negative_infinity_for_zero_defect_rate() -> None:
    assert log_defect_rate(0, 100) == float("-inf")


def test_log_defect_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        log_defect_rate(11, 10)

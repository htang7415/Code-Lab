from __future__ import annotations

import math

import pytest

from log_escape_rate import log_escape_rate


def test_log_escape_rate_returns_log_of_escape_rate() -> None:
    assert log_escape_rate(12, 600) == pytest.approx(math.log(0.02))


def test_log_escape_rate_returns_negative_infinity_for_zero_escape_rate() -> None:
    assert log_escape_rate(0, 600) == float("-inf")


def test_log_escape_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="escape_count"):
        log_escape_rate(601, 600)

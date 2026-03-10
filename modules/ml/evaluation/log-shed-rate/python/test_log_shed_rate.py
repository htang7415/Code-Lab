from __future__ import annotations

import math

import pytest

from log_shed_rate import log_shed_rate


def test_log_shed_rate_returns_log_of_shed_rate() -> None:
    assert log_shed_rate(5, 250) == pytest.approx(math.log(0.02))


def test_log_shed_rate_returns_negative_infinity_for_zero_shed_rate() -> None:
    assert log_shed_rate(0, 250) == float("-inf")


def test_log_shed_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="shed_count"):
        log_shed_rate(251, 250)

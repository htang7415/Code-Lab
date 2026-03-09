from __future__ import annotations

import math

import pytest

from log_event_rate import log_event_rate


def test_log_event_rate_returns_log_of_rate() -> None:
    score = log_event_rate(20, 100)

    assert score == pytest.approx(math.log(0.2))


def test_log_event_rate_returns_negative_infinity_for_zero_event_rate() -> None:
    assert log_event_rate(0, 100) == float("-inf")


def test_log_event_rate_rejects_non_positive_total_count() -> None:
    with pytest.raises(ValueError, match="positive"):
        log_event_rate(1, 0)

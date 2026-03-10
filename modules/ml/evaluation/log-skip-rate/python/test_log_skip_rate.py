from __future__ import annotations

import math

import pytest

from log_skip_rate import log_skip_rate


def test_log_skip_rate_returns_log_of_skip_rate() -> None:
    assert log_skip_rate(4, 200) == pytest.approx(math.log(0.02))


def test_log_skip_rate_returns_negative_infinity_for_zero_skip_rate() -> None:
    assert log_skip_rate(0, 200) == float("-inf")


def test_log_skip_rate_rejects_impossible_counts() -> None:
    with pytest.raises(ValueError, match="skip_count"):
        log_skip_rate(201, 200)

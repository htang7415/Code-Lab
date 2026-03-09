import math

import pytest

from log_risk_ratio import log_risk_ratio


def test_log_risk_ratio_returns_log_of_risk_ratio() -> None:
    value = log_risk_ratio([1, 0, 1, 1], [0, 1, 0, 0])

    assert value == pytest.approx(math.log(3.0))


def test_log_risk_ratio_returns_negative_infinity_for_zero_exposed_rate() -> None:
    assert log_risk_ratio([0, 0], [1, 0]) == float("-inf")


def test_log_risk_ratio_returns_zero_when_both_rates_are_zero() -> None:
    assert log_risk_ratio([], []) == pytest.approx(0.0)


def test_log_risk_ratio_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        log_risk_ratio([1, 2], [0, 1])

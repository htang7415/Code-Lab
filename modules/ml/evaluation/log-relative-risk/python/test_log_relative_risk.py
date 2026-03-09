import math

import pytest

from log_relative_risk import log_relative_risk


def test_log_relative_risk_returns_log_of_relative_risk() -> None:
    value = log_relative_risk([1, 0, 1, 1], [0, 1, 0, 0])

    assert value == pytest.approx(math.log(3.0))


def test_log_relative_risk_returns_negative_infinity_for_zero_exposed_rate() -> None:
    assert log_relative_risk([0, 0], [1, 0]) == float("-inf")


def test_log_relative_risk_returns_zero_when_both_rates_are_zero() -> None:
    assert log_relative_risk([], []) == pytest.approx(0.0)


def test_log_relative_risk_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        log_relative_risk([1, 2], [0, 1])

import math

import pytest

from log_odds import log_odds


def test_log_odds_returns_log_of_positive_odds() -> None:
    assert log_odds([1, 0, 1, 1]) == pytest.approx(math.log(3.0))


def test_log_odds_returns_negative_infinity_when_positive_rate_is_zero() -> None:
    assert log_odds([0, 0, 0]) == float("-inf")


def test_log_odds_returns_zero_for_empty_input() -> None:
    assert log_odds([]) == pytest.approx(0.0)


def test_log_odds_requires_binary_labels() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        log_odds([1, 2, 0])

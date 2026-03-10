from __future__ import annotations

import math

import pytest

from binary_rate_comparison_metrics import (
    base_rate_gap,
    base_rate_ratio,
    log_odds,
    log_prevalence_ratio,
    log_rate_ratio,
    log_relative_risk,
    log_risk_ratio,
    positive_rate,
    prevalence_delta,
    prevalence_index,
    prevalence_odds,
    prevalence_ratio,
    risk_ratio,
)


def test_positive_rate_and_gap_family_share_the_same_rate_primitive() -> None:
    assert positive_rate([1, 0, 1, 1, 0]) == pytest.approx(0.6)
    assert base_rate_gap([1, 0, 1, 1], [0, 1, 0, 0]) == pytest.approx(0.5)
    assert prevalence_delta([1, 0, 0, 1], [1, 1, 1, 0]) == pytest.approx(0.25)


def test_ratio_family_returns_expected_relative_effects() -> None:
    assert prevalence_ratio([1, 0, 1, 1], [0, 1, 0, 0]) == pytest.approx(3.0)
    assert risk_ratio([1, 1, 0, 1], [0, 1, 0, 0]) == pytest.approx(3.0)
    assert base_rate_ratio([1, 0, 1, 1], [0, 1, 0, 0]) == pytest.approx(3.0)
    assert prevalence_index([1, 0, 1, 1], baseline_rate=0.25) == pytest.approx(3.0)


def test_odds_and_log_family_handle_zero_and_nonzero_cases() -> None:
    assert prevalence_odds([1, 0, 1, 1]) == pytest.approx(3.0)
    assert log_odds([1, 0, 1, 1]) == pytest.approx(math.log(3.0))
    assert log_prevalence_ratio([1, 0, 1, 1], [0, 1, 0, 0]) == pytest.approx(math.log(3.0))
    assert log_risk_ratio([1, 0, 1, 1], [0, 1, 0, 0]) == pytest.approx(math.log(3.0))
    assert log_relative_risk([1, 0, 1, 1], [0, 1, 0, 0]) == pytest.approx(math.log(3.0))
    assert log_rate_ratio(30, 100, 10, 100) == pytest.approx(math.log(3.0))
    assert log_prevalence_ratio([0, 0], [1, 0]) == float("-inf")


def test_binary_rate_comparison_metrics_validate_inputs() -> None:
    with pytest.raises(ValueError, match="0 or 1"):
        positive_rate([1, 2, 0])
    with pytest.raises(ValueError, match="lie in"):
        prevalence_index([1, 0], baseline_rate=1.5)
    with pytest.raises(ValueError, match="cannot exceed"):
        log_rate_ratio(11, 10, 2, 10)

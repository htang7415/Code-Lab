from __future__ import annotations

import pytest

from cost_performance_tradeoffs import (
    cost_per_1k_requests,
    latency_improvement_ms,
    worthwhile_tradeoff,
)


def test_cost_per_1k_requests_normalizes_hourly_spend() -> None:
    assert cost_per_1k_requests(hourly_cost=12.0, requests_per_hour=60000) == pytest.approx(0.2)


def test_latency_improvement_ms_measures_saved_latency() -> None:
    assert latency_improvement_ms(baseline_ms=300, candidate_ms=220) == 80


def test_worthwhile_tradeoff_requires_positive_gain_and_acceptable_extra_cost() -> None:
    assert worthwhile_tradeoff(latency_gain_ms=80, extra_cost_per_1k=0.02, max_extra_cost_per_1k=0.03) is True
    assert worthwhile_tradeoff(latency_gain_ms=80, extra_cost_per_1k=0.05, max_extra_cost_per_1k=0.03) is False
    assert worthwhile_tradeoff(latency_gain_ms=0, extra_cost_per_1k=0.01, max_extra_cost_per_1k=0.03) is False

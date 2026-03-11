from __future__ import annotations

import pytest

from caching_basics import cache_hit_rate, should_cache, stale_risk


def test_should_cache_prefers_read_heavy_workloads_with_some_freshness_budget() -> None:
    assert should_cache(read_frequency=1000, mutation_frequency=5, freshness_tolerance_s=60) is True
    assert should_cache(read_frequency=20, mutation_frequency=10, freshness_tolerance_s=60) is False
    assert should_cache(read_frequency=1000, mutation_frequency=5, freshness_tolerance_s=0) is False


def test_cache_hit_rate_reports_fraction_of_served_lookups() -> None:
    assert cache_hit_rate(hits=900, lookups=1000) == pytest.approx(0.9)


def test_stale_risk_rises_with_mutation_pressure_and_freshness_window() -> None:
    assert stale_risk(mutation_frequency=0, freshness_tolerance_s=60) == "low"
    assert stale_risk(mutation_frequency=5, freshness_tolerance_s=5) == "medium"
    assert stale_risk(mutation_frequency=20, freshness_tolerance_s=5) == "high"

from __future__ import annotations

from strategy_pattern_in_real_systems import lowest_cost, lowest_latency, select_region


def test_select_region_supports_multiple_policies() -> None:
    candidates = [
        {"name": "us-east", "latency_ms": 40, "monthly_cost": 200},
        {"name": "eu-west", "latency_ms": 60, "monthly_cost": 120},
        {"name": "us-west", "latency_ms": 55, "monthly_cost": 180},
    ]

    assert select_region(candidates, lowest_latency) == "us-east"
    assert select_region(candidates, lowest_cost) == "eu-west"


def test_lowest_latency_breaks_ties_with_cost() -> None:
    candidates = [
        {"name": "region-a", "latency_ms": 45, "monthly_cost": 180},
        {"name": "region-b", "latency_ms": 45, "monthly_cost": 150},
    ]

    assert select_region(candidates, lowest_latency) == "region-b"


def test_lowest_cost_breaks_ties_with_latency() -> None:
    candidates = [
        {"name": "region-a", "latency_ms": 40, "monthly_cost": 100},
        {"name": "region-b", "latency_ms": 35, "monthly_cost": 100},
    ]

    assert select_region(candidates, lowest_cost) == "region-b"

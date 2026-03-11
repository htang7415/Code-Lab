from semantic_cache_hit_rate_analysis import (
    hit_rate,
    latency_saved_ms,
    savings_summary,
    scoped_hit_rates,
)


def test_hit_rates_can_be_computed_overall_and_by_scope():
    events = [
        {"workspace_id": 7, "hit": True},
        {"workspace_id": 7, "hit": False},
        {"workspace_id": 8, "hit": True},
    ]

    assert hit_rate(events) == 2 / 3
    assert scoped_hit_rates(events, "workspace_id") == {7: 0.5, 8: 1.0}


def test_latency_savings_links_hit_rate_to_actual_value():
    events = [
        {"workspace_id": 7, "hit": True},
        {"workspace_id": 7, "hit": False},
        {"workspace_id": 8, "hit": True},
    ]

    assert latency_saved_ms(events, hit_latency_ms=20, miss_latency_ms=200) == 360
    assert savings_summary(events, hit_latency_ms=20, miss_latency_ms=200) == {
        "request_count": 3,
        "hit_rate": 2 / 3,
        "latency_saved_ms": 360,
    }

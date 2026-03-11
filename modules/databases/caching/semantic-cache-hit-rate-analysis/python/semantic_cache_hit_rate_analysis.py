"""semantic_cache_hit_rate_analysis - measure whether semantic caching is paying off."""

from __future__ import annotations


def hit_rate(events: list[dict[str, object]]) -> float:
    if not events:
        return 0.0
    hits = sum(1 for event in events if bool(event["hit"]))
    return hits / len(events)


def scoped_hit_rates(
    events: list[dict[str, object]],
    scope_field: str,
) -> dict[object, float]:
    grouped: dict[object, list[dict[str, object]]] = {}
    for event in events:
        grouped.setdefault(event[scope_field], []).append(event)
    return {
        scope: hit_rate(group_events)
        for scope, group_events in grouped.items()
    }


def latency_saved_ms(
    events: list[dict[str, object]],
    hit_latency_ms: int,
    miss_latency_ms: int,
) -> int:
    baseline = len(events) * miss_latency_ms
    actual = sum(hit_latency_ms if bool(event["hit"]) else miss_latency_ms for event in events)
    return baseline - actual


def savings_summary(
    events: list[dict[str, object]],
    hit_latency_ms: int,
    miss_latency_ms: int,
) -> dict[str, float | int]:
    return {
        "request_count": len(events),
        "hit_rate": hit_rate(events),
        "latency_saved_ms": latency_saved_ms(events, hit_latency_ms, miss_latency_ms),
    }

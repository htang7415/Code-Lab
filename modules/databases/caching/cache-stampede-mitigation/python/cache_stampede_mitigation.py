"""cache_stampede_mitigation - single-flight refresh with stale-while-revalidate."""

from __future__ import annotations


def cache_entry(value: str, expires_at: int, stale_until: int) -> dict[str, object]:
    return {
        "value": value,
        "expires_at": expires_at,
        "stale_until": stale_until,
    }


def request_action(
    cache: dict[str, dict[str, object]],
    inflight: set[str],
    key: str,
    now: int,
) -> str:
    entry = cache.get(key)
    if entry is not None:
        if now < int(entry["expires_at"]):
            return "hit"
        if key in inflight:
            return "serve-stale" if now < int(entry["stale_until"]) else "wait"
        inflight.add(key)
        return "refresh"

    if key in inflight:
        return "wait"
    inflight.add(key)
    return "refresh"


def finish_refresh(
    cache: dict[str, dict[str, object]],
    inflight: set[str],
    key: str,
    value: str,
    now: int,
    ttl: int,
    stale_window: int,
) -> None:
    cache[key] = cache_entry(
        value=value,
        expires_at=now + ttl,
        stale_until=now + ttl + stale_window,
    )
    inflight.discard(key)

"""ttl_and_invalidation - time-based freshness plus explicit invalidation."""

from __future__ import annotations


Cache = dict[str, dict[str, object]]


def set_cache_entry(
    cache: Cache,
    key: str,
    value: object,
    now: int,
    ttl_seconds: int,
    tags: set[str] | None = None,
) -> None:
    cache[key] = {
        "value": value,
        "expires_at": now + ttl_seconds,
        "tags": set(tags or set()),
    }


def get_if_fresh(
    cache: Cache,
    key: str,
    now: int,
) -> object | None:
    entry = cache.get(key)
    if entry is None:
        return None
    if int(entry["expires_at"]) <= now:
        return None
    return entry["value"]


def invalidate_key(cache: Cache, key: str) -> None:
    cache.pop(key, None)


def invalidate_tag(cache: Cache, tag: str) -> None:
    doomed = [
        key
        for key, entry in cache.items()
        if tag in set(entry["tags"])
    ]
    for key in doomed:
        cache.pop(key, None)


def stale_keys(cache: Cache, now: int) -> list[str]:
    return sorted(
        key
        for key, entry in cache.items()
        if int(entry["expires_at"]) <= now
    )

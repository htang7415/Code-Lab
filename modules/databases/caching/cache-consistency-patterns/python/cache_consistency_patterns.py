"""cache_consistency_patterns - compare cache-aside, write-through, and invalidation."""

from __future__ import annotations


def cache_aside_read(
    store: dict[str, str],
    cache: dict[str, str],
    key: str,
) -> str | None:
    if key in cache:
        return cache[key]
    value = store.get(key)
    if value is not None:
        cache[key] = value
    return value


def write_through_update(
    store: dict[str, str],
    cache: dict[str, str],
    key: str,
    value: str,
) -> None:
    store[key] = value
    cache[key] = value


def invalidate_on_write_update(
    store: dict[str, str],
    cache: dict[str, str],
    key: str,
    value: str,
) -> None:
    store[key] = value
    cache.pop(key, None)


def stale_cache_keys(
    store: dict[str, str],
    cache: dict[str, str],
) -> list[str]:
    return sorted(
        key
        for key, value in cache.items()
        if store.get(key) != value
    )

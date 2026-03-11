"""cache_aside - minimal cache-aside pattern with TTL and invalidation."""

from __future__ import annotations

from collections.abc import Callable


Cache = dict[str, tuple[object, int | None]]


def read_through_cache(
    cache: Cache,
    key: str,
    loader: Callable[[], object],
    now: int,
    ttl_seconds: int | None = None,
) -> object:
    entry = cache.get(key)
    if entry is not None:
        value, expires_at = entry
        if expires_at is None or now < expires_at:
            return value

    value = loader()
    expires_at = None if ttl_seconds is None else now + ttl_seconds
    cache[key] = (value, expires_at)
    return value


def invalidate(cache: Cache, key: str) -> None:
    cache.pop(key, None)

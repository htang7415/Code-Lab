"""cache_ttl_jitter - spread expirations with deterministic TTL offsets."""

from __future__ import annotations


def stable_jitter_seconds(key: str, base_ttl: int, jitter_ratio: float) -> int:
    if not 0.0 <= jitter_ratio <= 1.0:
        raise ValueError("jitter_ratio must be between 0 and 1")
    spread = int(base_ttl * jitter_ratio)
    if spread == 0:
        return 0
    stable_hash = sum((index + 1) * ord(char) for index, char in enumerate(key))
    return (stable_hash % (2 * spread + 1)) - spread


def expiration_time(
    key: str,
    now: int,
    base_ttl: int,
    jitter_ratio: float,
) -> int:
    return now + base_ttl + stable_jitter_seconds(key, base_ttl, jitter_ratio)


def jittered_expirations(
    keys: list[str],
    now: int,
    base_ttl: int,
    jitter_ratio: float,
) -> dict[str, int]:
    return {
        key: expiration_time(key, now, base_ttl, jitter_ratio)
        for key in keys
    }


def expiration_bucket_counts(expirations: dict[str, int]) -> dict[int, int]:
    buckets: dict[int, int] = {}
    for expires_at in expirations.values():
        buckets[int(expires_at)] = buckets.get(int(expires_at), 0) + 1
    return buckets


def max_bucket_load(expirations: dict[str, int]) -> int:
    buckets = expiration_bucket_counts(expirations)
    return 0 if not buckets else max(buckets.values())

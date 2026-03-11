import pytest

from cache_ttl_jitter import (
    expiration_bucket_counts,
    jittered_expirations,
    max_bucket_load,
    stable_jitter_seconds,
)


def test_jitter_spreads_key_expirations_across_multiple_buckets():
    keys = ["k1", "k2", "k3", "k4", "k5", "k6"]
    expirations = jittered_expirations(keys, now=100, base_ttl=60, jitter_ratio=0.2)

    assert len(set(expirations.values())) > 1
    assert max_bucket_load(expirations) < len(keys)
    assert sum(expiration_bucket_counts(expirations).values()) == len(keys)


def test_invalid_jitter_ratio_raises():
    with pytest.raises(ValueError):
        stable_jitter_seconds("k1", base_ttl=60, jitter_ratio=1.5)

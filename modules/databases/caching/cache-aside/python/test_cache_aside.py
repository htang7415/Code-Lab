from cache_aside import invalidate, read_through_cache


def test_cache_hit_avoids_reloading_before_ttl_expires() -> None:
    cache = {}
    calls = {"count": 0}

    def loader() -> dict[str, object]:
        calls["count"] += 1
        return {"name": "Ada"}

    first = read_through_cache(cache, "user:42", loader, now=100, ttl_seconds=30)
    second = read_through_cache(cache, "user:42", loader, now=110, ttl_seconds=30)

    assert first == second == {"name": "Ada"}
    assert calls["count"] == 1


def test_expired_entry_is_loaded_again() -> None:
    cache = {}
    calls = {"count": 0}

    def loader() -> int:
        calls["count"] += 1
        return calls["count"]

    first = read_through_cache(cache, "report", loader, now=100, ttl_seconds=10)
    second = read_through_cache(cache, "report", loader, now=111, ttl_seconds=10)

    assert (first, second) == (1, 2)
    assert calls["count"] == 2


def test_invalidation_forces_a_refresh_even_before_ttl_expiry() -> None:
    cache = {}
    calls = {"count": 0}

    def loader() -> int:
        calls["count"] += 1
        return calls["count"]

    first = read_through_cache(cache, "settings", loader, now=100, ttl_seconds=60)
    invalidate(cache, "settings")
    second = read_through_cache(cache, "settings", loader, now=101, ttl_seconds=60)

    assert (first, second) == (1, 2)

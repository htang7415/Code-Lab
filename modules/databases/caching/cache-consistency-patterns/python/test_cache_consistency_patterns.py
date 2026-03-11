from cache_consistency_patterns import (
    cache_aside_read,
    invalidate_on_write_update,
    stale_cache_keys,
    write_through_update,
)


def test_cache_aside_can_become_stale_if_store_changes_behind_cache():
    store = {"doc:1": "old"}
    cache: dict[str, str] = {}

    assert cache_aside_read(store, cache, "doc:1") == "old"
    store["doc:1"] = "new"

    assert stale_cache_keys(store, cache) == ["doc:1"]
    assert cache_aside_read(store, cache, "doc:1") == "old"


def test_write_through_and_invalidate_on_write_avoid_stale_copy():
    store = {"doc:1": "old", "doc:2": "old"}
    cache = {"doc:1": "old", "doc:2": "old"}

    write_through_update(store, cache, "doc:1", "new")
    invalidate_on_write_update(store, cache, "doc:2", "new")

    assert stale_cache_keys(store, cache) == []
    assert cache["doc:1"] == "new"
    assert "doc:2" not in cache
    assert cache_aside_read(store, cache, "doc:2") == "new"

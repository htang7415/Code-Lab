from ttl_and_invalidation import (
    get_if_fresh,
    invalidate_key,
    invalidate_tag,
    set_cache_entry,
    stale_keys,
)
import pytest


def test_entry_is_fresh_until_its_ttl_expires() -> None:
    cache = {}
    set_cache_entry(cache, "doc:1", {"title": "Spec"}, now=100, ttl_seconds=30)

    assert get_if_fresh(cache, "doc:1", now=129) == {"title": "Spec"}
    assert get_if_fresh(cache, "doc:1", now=130) is None


def test_tag_invalidation_removes_all_related_entries() -> None:
    cache = {}
    set_cache_entry(cache, "doc:1", 1, now=100, ttl_seconds=30, tags={"workspace:7"})
    set_cache_entry(cache, "doc:2", 2, now=100, ttl_seconds=30, tags={"workspace:7", "doc-list"})
    set_cache_entry(cache, "doc:3", 3, now=100, ttl_seconds=30, tags={"workspace:8"})

    invalidate_tag(cache, "workspace:7")

    assert sorted(cache.keys()) == ["doc:3"]


def test_stale_keys_and_single_key_invalidation_work_together() -> None:
    cache = {}
    set_cache_entry(cache, "doc:1", 1, now=100, ttl_seconds=5)
    set_cache_entry(cache, "doc:2", 2, now=100, ttl_seconds=50)

    assert stale_keys(cache, now=106) == ["doc:1"]
    invalidate_key(cache, "doc:2")
    assert sorted(cache.keys()) == ["doc:1"]


def test_ttl_must_be_positive() -> None:
    with pytest.raises(ValueError, match="ttl_seconds"):
        set_cache_entry({}, "doc:1", 1, now=100, ttl_seconds=0)

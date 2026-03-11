from cache_key_design import cache_key, key_collides, naive_key, parse_cache_key
import pytest


def test_scoped_versioned_keys_separate_tenants_and_versions():
    left = cache_key("answer", 7, "doc-42", "v1")
    right = cache_key("answer", 8, "doc-42", "v1")
    newer = cache_key("answer", 7, "doc-42", "v2")

    assert not key_collides(left, right)
    assert not key_collides(left, newer)
    assert parse_cache_key(left) == {
        "namespace": "answer",
        "ws": 7,
        "id": "doc-42",
        "v": "v1",
    }


def test_sorted_extras_make_equivalent_requests_share_one_key():
    first = cache_key(
        "answer",
        7,
        "doc-42",
        "v2",
        extras={"lang": "en", "mode": "summary"},
    )
    second = cache_key(
        "answer",
        7,
        "doc-42",
        "v2",
        extras={"mode": "summary", "lang": "en"},
    )

    assert first == second
    assert key_collides(naive_key("doc-42"), naive_key("doc-42"))


def test_reserved_delimiters_and_negative_workspace_ids_are_rejected():
    with pytest.raises(ValueError, match="resource_id"):
        cache_key("answer", 7, "doc|42", "v1")

    with pytest.raises(ValueError, match="workspace_id"):
        cache_key("answer", -1, "doc-42", "v1")

    with pytest.raises(ValueError, match="contain"):
        cache_key("answer", 7, "doc-42", "v1", extras={"mode": "summary=short"})

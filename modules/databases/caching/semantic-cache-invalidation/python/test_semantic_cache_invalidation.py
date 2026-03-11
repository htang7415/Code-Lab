from semantic_cache_invalidation import (
    invalidate_scope,
    lookup_semantic_cache,
    store_semantic_entry,
)


def test_lookup_requires_matching_policy_and_source_versions():
    entries: list[dict[str, object]] = []
    store_semantic_entry(
        entries,
        "show failed jobs",
        "2 failed jobs",
        workspace_id=7,
        policy_version="policy-v1",
        source_version="docs-v1",
        now=100,
    )

    assert (
        lookup_semantic_cache(
            entries,
            "failed jobs",
            workspace_id=7,
            policy_version="policy-v1",
            source_version="docs-v1",
            now=120,
        )
        == "2 failed jobs"
    )
    assert (
        lookup_semantic_cache(
            entries,
            "failed jobs",
            workspace_id=7,
            policy_version="policy-v1",
            source_version="docs-v2",
            now=120,
        )
        is None
    )


def test_invalidate_scope_removes_only_stale_entries_for_one_workspace():
    entries: list[dict[str, object]] = []
    store_semantic_entry(entries, "q1", "r1", 7, "policy-v1", "docs-v1", now=10)
    store_semantic_entry(entries, "q2", "r2", 7, "policy-v2", "docs-v2", now=20)
    store_semantic_entry(entries, "q3", "r3", 8, "policy-v1", "docs-v1", now=30)

    removed = invalidate_scope(
        entries,
        workspace_id=7,
        current_policy_version="policy-v2",
        current_source_version="docs-v2",
    )

    assert removed == 1
    assert [entry["response"] for entry in entries] == ["r2", "r3"]

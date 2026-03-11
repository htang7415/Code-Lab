from jsonb_and_gin_indexing import (
    build_metadata_inverted_index,
    filter_documents_with_index,
    update_term_diff,
)


DOCUMENTS = [
    {"id": "doc-1", "metadata": {"language": "en", "tags": ["rag", "eval"]}},
    {"id": "doc-2", "metadata": {"language": "en", "tags": ["security"]}},
    {"id": "doc-3", "metadata": {"language": "fr", "tags": ["rag"]}},
]


def test_inverted_index_supports_multi_term_intersection() -> None:
    inverted = build_metadata_inverted_index(DOCUMENTS)

    assert filter_documents_with_index(inverted, ["language=en", "tag=rag"]) == ["doc-1"]
    assert filter_documents_with_index(inverted, ["tag=rag"]) == ["doc-1", "doc-3"]


def test_missing_term_returns_no_matches() -> None:
    inverted = build_metadata_inverted_index(DOCUMENTS)

    assert filter_documents_with_index(inverted, ["language=de"]) == []


def test_term_diff_shows_the_index_updates_needed_for_metadata_changes() -> None:
    removed, added = update_term_diff(
        {"id": "doc-1", "metadata": {"language": "en", "tags": ["rag", "eval"]}},
        {"id": "doc-1", "metadata": {"language": "en", "tags": ["security"]}},
    )

    assert removed == {"tag=rag", "tag=eval"}
    assert added == {"tag=security"}

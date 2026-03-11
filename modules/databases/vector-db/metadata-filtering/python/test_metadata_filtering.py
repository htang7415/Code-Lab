from metadata_filtering import matches_filters, top_k_with_metadata


DOCUMENTS = [
    {"id": "a", "workspace_id": 7, "doc_type": "spec", "vector": [1.0, 0.0]},
    {"id": "b", "workspace_id": 7, "doc_type": "note", "vector": [0.95, 0.05]},
    {"id": "c", "workspace_id": 8, "doc_type": "spec", "vector": [0.99, 0.01]},
    {"id": "d", "workspace_id": 7, "doc_type": "spec", "vector": [0.8, 0.2]},
]


def test_filter_predicate_requires_all_metadata_constraints() -> None:
    assert matches_filters(DOCUMENTS[0], {"workspace_id": 7, "doc_type": "spec"}) is True
    assert matches_filters(DOCUMENTS[1], {"workspace_id": 7, "doc_type": "spec"}) is False


def test_top_k_search_ignores_wrong_tenant_or_wrong_type_even_if_similarity_is_high() -> None:
    assert top_k_with_metadata(
        query_vector=[1.0, 0.0],
        documents=DOCUMENTS,
        filters={"workspace_id": 7, "doc_type": "spec"},
        k=2,
    ) == [
        ("a", 1.0),
        ("d", 0.9701425001453318),
    ]


def test_empty_filter_result_returns_no_candidates() -> None:
    assert top_k_with_metadata(
        query_vector=[1.0, 0.0],
        documents=DOCUMENTS,
        filters={"workspace_id": 9},
        k=2,
    ) == []

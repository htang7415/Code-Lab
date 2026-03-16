from __future__ import annotations

import pytest

from hnsw_graph_search import (
    build_hnsw_layer0,
    greedy_entrypoint,
    hnsw_candidate_ids,
)


DOCUMENTS = [
    {"id": "a", "vector": [1.0, 0.0]},
    {"id": "b", "vector": [0.9, 0.1]},
    {"id": "c", "vector": [0.1, 0.9]},
    {"id": "d", "vector": [0.0, 1.0]},
]


def test_greedy_entrypoint_picks_the_most_central_document() -> None:
    assert greedy_entrypoint(DOCUMENTS) == "b"


def test_build_hnsw_layer0_connects_each_document_to_nearest_neighbors() -> None:
    graph = build_hnsw_layer0(DOCUMENTS, max_neighbors=2)

    assert graph["b"] == ["a", "c"]
    assert graph["c"] == ["d", "b"]


def test_hnsw_candidate_ids_expand_toward_the_query_neighborhood() -> None:
    candidates = hnsw_candidate_ids(
        query_vector=[0.0, 1.0],
        documents=DOCUMENTS,
        max_neighbors=2,
        ef_search=3,
    )

    assert candidates == ["d", "c", "b"]


def test_invalid_search_parameters_are_rejected() -> None:
    with pytest.raises(ValueError, match="max_neighbors"):
        build_hnsw_layer0(DOCUMENTS, max_neighbors=0)

    with pytest.raises(ValueError, match="ef_search"):
        hnsw_candidate_ids([0.0, 1.0], DOCUMENTS, ef_search=0)

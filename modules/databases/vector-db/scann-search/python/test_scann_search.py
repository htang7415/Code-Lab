from __future__ import annotations

import pytest

from scann_search import (
    assign_leaves,
    dominant_axis,
    leaf_order,
    scann_candidate_ids,
)


DOCUMENTS = [
    {"id": "x1", "vector": [0.95, 0.05]},
    {"id": "x2", "vector": [0.80, 0.20]},
    {"id": "y1", "vector": [0.15, 0.85]},
    {"id": "y2", "vector": [0.05, 0.95]},
]

QUERY = [0.10, 0.90]


def test_dominant_axis_and_leaf_order_follow_largest_coordinate() -> None:
    assert dominant_axis([0.8, 0.2]) == 0
    assert dominant_axis([0.2, 0.8]) == 1
    assert leaf_order(QUERY) == [1, 0]


def test_assign_leaves_groups_documents_by_dominant_axis() -> None:
    assert assign_leaves(DOCUMENTS) == {0: ["x1", "x2"], 1: ["y1", "y2"]}


def test_scann_candidate_ids_probe_few_leaves_then_reorder_candidates() -> None:
    assert scann_candidate_ids(QUERY, DOCUMENTS, leaves_to_search=1, reorder_k=2) == [
        "y2",
        "y1",
    ]
    assert scann_candidate_ids(QUERY, DOCUMENTS, leaves_to_search=2, reorder_k=3) == [
        "y2",
        "y1",
        "x2",
    ]


def test_invalid_scann_parameters_are_rejected() -> None:
    with pytest.raises(ValueError, match="leaves_to_search"):
        scann_candidate_ids(QUERY, DOCUMENTS, leaves_to_search=0, reorder_k=2)

    with pytest.raises(ValueError, match="reorder_k"):
        scann_candidate_ids(QUERY, DOCUMENTS, leaves_to_search=1, reorder_k=-1)

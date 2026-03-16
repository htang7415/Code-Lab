from __future__ import annotations

import pytest

from ivf_search import (
    build_inverted_lists,
    ivf_candidate_ids,
    nearest_centroid_id,
    probed_centroid_ids,
)


CENTROIDS = [
    {"id": "c1", "vector": [1.0, 0.0]},
    {"id": "c2", "vector": [0.0, 1.0]},
]

DOCUMENTS = [
    {"id": "d1", "vector": [0.95, 0.05]},
    {"id": "d2", "vector": [0.85, 0.15]},
    {"id": "d3", "vector": [0.10, 0.90]},
    {"id": "d4", "vector": [0.20, 0.80]},
]

QUERY = [0.05, 0.95]


def test_nearest_centroid_id_assigns_documents_to_the_expected_list() -> None:
    assert nearest_centroid_id([0.92, 0.08], CENTROIDS) == "c1"
    assert nearest_centroid_id([0.08, 0.92], CENTROIDS) == "c2"


def test_build_inverted_lists_groups_documents_by_centroid() -> None:
    lists = build_inverted_lists(DOCUMENTS, CENTROIDS)
    assert lists == {"c1": ["d1", "d2"], "c2": ["d3", "d4"]}


def test_probed_centroid_ids_and_candidates_follow_nprobe() -> None:
    assert probed_centroid_ids(QUERY, CENTROIDS, nprobe=1) == ["c2"]
    assert ivf_candidate_ids(QUERY, DOCUMENTS, CENTROIDS, nprobe=1) == ["d3", "d4"]


def test_invalid_nprobe_is_rejected() -> None:
    with pytest.raises(ValueError, match="positive"):
        probed_centroid_ids(QUERY, CENTROIDS, nprobe=0)

    with pytest.raises(ValueError, match="cannot exceed"):
        probed_centroid_ids(QUERY, CENTROIDS, nprobe=3)

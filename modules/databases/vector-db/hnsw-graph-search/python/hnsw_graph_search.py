"""hnsw_graph_search - toy HNSW-style graph expansion over vector neighbors."""

from __future__ import annotations

import math


def validate_vector(vector: list[float]) -> None:
    if not vector:
        raise ValueError("vector must be non-empty")


def cosine_similarity(left: list[float], right: list[float]) -> float:
    validate_vector(left)
    validate_vector(right)
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimensions")
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0.0 or right_norm == 0.0:
        return 0.0
    return sum(a * b for a, b in zip(left, right)) / (left_norm * right_norm)


def greedy_entrypoint(documents: list[dict[str, object]]) -> str:
    if not documents:
        raise ValueError("documents must be non-empty")

    scores: list[tuple[str, float]] = []
    for document in documents:
        doc_id = str(document["id"])
        vector = list(document["vector"])
        validate_vector(vector)
        similarities = [
            cosine_similarity(vector, list(other["vector"]))
            for other in documents
            if other is not document
        ]
        average_similarity = (
            sum(similarities) / len(similarities) if similarities else 0.0
        )
        scores.append((doc_id, average_similarity))

    scores.sort(key=lambda item: (-item[1], item[0]))
    return scores[0][0]


def build_hnsw_layer0(
    documents: list[dict[str, object]],
    max_neighbors: int = 2,
) -> dict[str, list[str]]:
    if max_neighbors <= 0:
        raise ValueError("max_neighbors must be positive")

    graph: dict[str, list[str]] = {}
    for document in documents:
        doc_id = str(document["id"])
        vector = list(document["vector"])
        validate_vector(vector)
        neighbors: list[tuple[str, float]] = []
        for other in documents:
            if other is document:
                continue
            other_id = str(other["id"])
            other_vector = list(other["vector"])
            neighbors.append((other_id, cosine_similarity(vector, other_vector)))
        neighbors.sort(key=lambda item: (-item[1], item[0]))
        graph[doc_id] = [neighbor_id for neighbor_id, _ in neighbors[:max_neighbors]]
    return graph


def hnsw_candidate_ids(
    query_vector: list[float],
    documents: list[dict[str, object]],
    max_neighbors: int = 2,
    ef_search: int = 4,
) -> list[str]:
    validate_vector(query_vector)
    if ef_search <= 0:
        raise ValueError("ef_search must be positive")
    if not documents:
        return []

    graph = build_hnsw_layer0(documents, max_neighbors=max_neighbors)
    vectors = {
        str(document["id"]): list(document["vector"])
        for document in documents
    }

    frontier = [greedy_entrypoint(documents)]
    seen = set(frontier)
    visited: list[str] = []

    while frontier and len(visited) < ef_search:
        frontier.sort(
            key=lambda doc_id: (
                -cosine_similarity(query_vector, vectors[doc_id]),
                doc_id,
            )
        )
        current = frontier.pop(0)
        visited.append(current)
        for neighbor_id in graph[current]:
            if neighbor_id not in seen:
                seen.add(neighbor_id)
                frontier.append(neighbor_id)

    visited.sort(
        key=lambda doc_id: (-cosine_similarity(query_vector, vectors[doc_id]), doc_id)
    )
    return visited

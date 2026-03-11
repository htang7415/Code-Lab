"""metadata_filtering - similarity search constrained by metadata filters."""

from __future__ import annotations

import math


def cosine_similarity(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimensions")
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    similarity = sum(a * b for a, b in zip(left, right)) / (left_norm * right_norm)
    if abs(similarity - 1.0) < 1e-12:
        return 1.0
    if abs(similarity + 1.0) < 1e-12:
        return -1.0
    return similarity


def matches_filters(document: dict[str, object], filters: dict[str, object]) -> bool:
    return all(document.get(key) == value for key, value in filters.items())


def top_k_with_metadata(
    query_vector: list[float],
    documents: list[dict[str, object]],
    filters: dict[str, object],
    k: int,
) -> list[tuple[str, float]]:
    scored = [
        (
            str(document["id"]),
            cosine_similarity(query_vector, list(document["vector"])),
        )
        for document in documents
        if matches_filters(document, filters)
    ]
    return sorted(scored, key=lambda item: (-item[1], item[0]))[:k]

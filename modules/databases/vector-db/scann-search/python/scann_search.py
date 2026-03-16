"""scann_search - toy partition-and-reorder vector retrieval."""

from __future__ import annotations


def validate_vector(vector: list[float]) -> None:
    if not vector:
        raise ValueError("vector must be non-empty")


def dot_product(left: list[float], right: list[float]) -> float:
    validate_vector(left)
    validate_vector(right)
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimensions")
    return sum(a * b for a, b in zip(left, right))


def dominant_axis(vector: list[float]) -> int:
    validate_vector(vector)
    return sorted(range(len(vector)), key=lambda index: (-vector[index], index))[0]


def assign_leaves(documents: list[dict[str, object]]) -> dict[int, list[str]]:
    leaves: dict[int, list[str]] = {}
    for document in documents:
        axis = dominant_axis(list(document["vector"]))
        leaves.setdefault(axis, []).append(str(document["id"]))
    return leaves


def leaf_order(query_vector: list[float]) -> list[int]:
    validate_vector(query_vector)
    return sorted(range(len(query_vector)), key=lambda index: (-query_vector[index], index))


def scann_candidate_ids(
    query_vector: list[float],
    documents: list[dict[str, object]],
    leaves_to_search: int = 1,
    reorder_k: int = 2,
) -> list[str]:
    validate_vector(query_vector)
    if leaves_to_search <= 0:
        raise ValueError("leaves_to_search must be positive")
    if reorder_k < 0:
        raise ValueError("reorder_k must be non-negative")
    if not documents or reorder_k == 0:
        return []

    leaves = assign_leaves(documents)
    ordered_leaves = leaf_order(query_vector)
    probe_set = set(ordered_leaves[:leaves_to_search])

    scored: list[tuple[str, float]] = []
    for document in documents:
        if dominant_axis(list(document["vector"])) not in probe_set:
            continue
        scored.append(
            (
                str(document["id"]),
                dot_product(query_vector, list(document["vector"])),
            )
        )
    scored.sort(key=lambda item: (-item[1], item[0]))
    return [doc_id for doc_id, _ in scored[:reorder_k]]

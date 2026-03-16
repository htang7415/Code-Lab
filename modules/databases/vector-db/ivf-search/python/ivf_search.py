"""ivf_search - toy IVF partitioning and probing for vector search."""

from __future__ import annotations


def validate_vector(vector: list[float]) -> None:
    if not vector:
        raise ValueError("vector must be non-empty")


def squared_l2_distance(left: list[float], right: list[float]) -> float:
    validate_vector(left)
    validate_vector(right)
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimensions")
    return sum((a - b) ** 2 for a, b in zip(left, right))


def nearest_centroid_id(
    vector: list[float],
    centroids: list[dict[str, object]],
) -> str:
    if not centroids:
        raise ValueError("centroids must be non-empty")
    distances = [
        (str(centroid["id"]), squared_l2_distance(vector, list(centroid["vector"])))
        for centroid in centroids
    ]
    distances.sort(key=lambda item: (item[1], item[0]))
    return distances[0][0]


def build_inverted_lists(
    documents: list[dict[str, object]],
    centroids: list[dict[str, object]],
) -> dict[str, list[str]]:
    lists = {str(centroid["id"]): [] for centroid in centroids}
    for document in documents:
        centroid_id = nearest_centroid_id(list(document["vector"]), centroids)
        lists[centroid_id].append(str(document["id"]))
    return lists


def probed_centroid_ids(
    query_vector: list[float],
    centroids: list[dict[str, object]],
    nprobe: int,
) -> list[str]:
    validate_vector(query_vector)
    if nprobe <= 0:
        raise ValueError("nprobe must be positive")
    if nprobe > len(centroids):
        raise ValueError("nprobe cannot exceed the number of centroids")

    distances = [
        (str(centroid["id"]), squared_l2_distance(query_vector, list(centroid["vector"])))
        for centroid in centroids
    ]
    distances.sort(key=lambda item: (item[1], item[0]))
    return [centroid_id for centroid_id, _ in distances[:nprobe]]


def ivf_candidate_ids(
    query_vector: list[float],
    documents: list[dict[str, object]],
    centroids: list[dict[str, object]],
    nprobe: int,
) -> list[str]:
    probe_ids = set(probed_centroid_ids(query_vector, centroids, nprobe))
    candidates: list[tuple[str, float]] = []
    for document in documents:
        doc_vector = list(document["vector"])
        centroid_id = nearest_centroid_id(doc_vector, centroids)
        if centroid_id not in probe_ids:
            continue
        candidates.append(
            (
                str(document["id"]),
                squared_l2_distance(query_vector, doc_vector),
            )
        )
    candidates.sort(key=lambda item: (item[1], item[0]))
    return [doc_id for doc_id, _ in candidates]

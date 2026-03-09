from __future__ import annotations


def retrieval_hit_rate_at_k(
    query_retrievals: list[list[str]],
    query_relevants: list[set[str]],
    k: int,
) -> float:
    if len(query_retrievals) != len(query_relevants):
        raise ValueError("query_retrievals and query_relevants must have the same length")
    if k <= 0:
        raise ValueError("k must be positive")
    if not query_retrievals:
        return 0.0

    hits = 0
    for retrieved_ids, relevant_ids in zip(query_retrievals, query_relevants):
        if set(retrieved_ids[:k]) & relevant_ids:
            hits += 1
    return hits / len(query_retrievals)

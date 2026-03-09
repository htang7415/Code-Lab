from __future__ import annotations


def retrieval_precision_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    if not retrieved_ids:
        return 0.0

    retrieved_top_k = set(retrieved_ids[:k])
    return len(retrieved_top_k & relevant_ids) / k

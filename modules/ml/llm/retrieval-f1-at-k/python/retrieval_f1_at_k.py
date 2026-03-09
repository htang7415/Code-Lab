from __future__ import annotations


def retrieval_f1_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    if not relevant_ids:
        return 0.0

    retrieved_top_k = set(retrieved_ids[:k])
    precision = len(retrieved_top_k & relevant_ids) / k
    recall = len(retrieved_top_k & relevant_ids) / len(relevant_ids)
    if precision + recall == 0.0:
        return 0.0
    return 2.0 * precision * recall / (precision + recall)

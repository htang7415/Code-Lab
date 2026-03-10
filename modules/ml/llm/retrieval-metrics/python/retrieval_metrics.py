from __future__ import annotations


def retrieval_recall_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    if not relevant_ids:
        return 0.0
    retrieved_top_k = set(retrieved_ids[:k])
    return len(retrieved_top_k & relevant_ids) / len(relevant_ids)


def retrieval_precision_at_k(retrieved_ids: list[str], relevant_ids: set[str], k: int) -> float:
    if k <= 0:
        raise ValueError("k must be positive")
    if not retrieved_ids:
        return 0.0
    retrieved_top_k = set(retrieved_ids[:k])
    return len(retrieved_top_k & relevant_ids) / k


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


def reciprocal_rank(relevance: list[int]) -> float:
    if any(label not in {0, 1} for label in relevance):
        raise ValueError("relevance labels must be binary")

    first_rank = next((index + 1 for index, label in enumerate(relevance) if label == 1), None)
    return 0.0 if first_rank is None else 1.0 / first_rank


def reranker_metrics(relevance: list[int], k: int) -> tuple[float, float]:
    if k <= 0:
        raise ValueError("k must be positive")
    if any(label not in {0, 1} for label in relevance):
        raise ValueError("relevance labels must be binary")
    if not relevance:
        return 0.0, 0.0

    top_k = relevance[:k]
    total_relevant = sum(relevance)
    recall = 0.0 if total_relevant == 0 else sum(top_k) / total_relevant
    return reciprocal_rank(top_k), recall


def rerank_gain(baseline_relevance: list[int], reranked_relevance: list[int]) -> float:
    return reciprocal_rank(reranked_relevance) - reciprocal_rank(baseline_relevance)


def rerank_disagreement_rate(
    baseline_ids: list[str],
    reranked_ids: list[str],
    k: int | None = None,
) -> float:
    if len(baseline_ids) != len(reranked_ids):
        raise ValueError("baseline_ids and reranked_ids must have the same length")
    if k is None:
        k = len(baseline_ids)
    if k <= 0:
        raise ValueError("k must be positive")
    if k > len(baseline_ids):
        raise ValueError("k cannot exceed ranking length")

    disagreements = sum(
        baseline_id != reranked_id
        for baseline_id, reranked_id in zip(baseline_ids[:k], reranked_ids[:k])
    )
    return disagreements / k

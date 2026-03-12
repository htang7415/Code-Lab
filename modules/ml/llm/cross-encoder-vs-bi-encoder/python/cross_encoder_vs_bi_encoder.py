"""cross_encoder_vs_bi_encoder - compare scalable embedding retrieval with pairwise reranking."""

from __future__ import annotations

import math


def cosine_similarity(left: list[float], right: list[float]) -> float:
    if len(left) != len(right):
        raise ValueError("left and right must have the same length")
    if not left:
        raise ValueError("left and right must be non-empty")

    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0.0 or right_norm == 0.0:
        return 0.0

    dot = sum(left_value * right_value for left_value, right_value in zip(left, right))
    return dot / (left_norm * right_norm)


def bi_encoder_score(query_embedding: list[float], document_embedding: list[float]) -> float:
    return cosine_similarity(query_embedding, document_embedding)


def _normalize_tokens(tokens: list[str]) -> list[str]:
    return [token.strip().lower() for token in tokens if token.strip()]


def cross_encoder_score(query_tokens: list[str], document_tokens: list[str]) -> float:
    query = _normalize_tokens(query_tokens)
    document = _normalize_tokens(document_tokens)
    if not query or not document:
        return 0.0

    query_set = set(query)
    document_set = set(document)
    coverage = len(query_set & document_set) / len(query_set)

    query_bigrams = list(zip(query, query[1:]))
    if not query_bigrams:
        order_bonus = 1.0 if query[0] in document_set else 0.0
    else:
        document_bigrams = set(zip(document, document[1:]))
        order_bonus = sum(1 for bigram in query_bigrams if bigram in document_bigrams) / len(query_bigrams)

    return 0.7 * coverage + 0.3 * order_bonus


def cross_encoder_full_corpus_pairs(num_queries: int, corpus_size: int) -> int:
    if num_queries < 0:
        raise ValueError("num_queries must be non-negative")
    if corpus_size < 0:
        raise ValueError("corpus_size must be non-negative")
    return num_queries * corpus_size


def bi_encoder_rerank_pairs(num_queries: int, candidate_k: int) -> int:
    if num_queries < 0:
        raise ValueError("num_queries must be non-negative")
    if candidate_k < 0:
        raise ValueError("candidate_k must be non-negative")
    return num_queries * candidate_k


def rerank_pair_reduction(corpus_size: int, candidate_k: int) -> float:
    if corpus_size <= 0:
        raise ValueError("corpus_size must be positive")
    if candidate_k < 0:
        raise ValueError("candidate_k must be non-negative")
    if candidate_k > corpus_size:
        raise ValueError("candidate_k cannot exceed corpus_size")
    return 1.0 - candidate_k / corpus_size

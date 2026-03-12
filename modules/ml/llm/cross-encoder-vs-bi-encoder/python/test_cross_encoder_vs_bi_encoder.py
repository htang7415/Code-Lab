from __future__ import annotations

import pytest

from cross_encoder_vs_bi_encoder import (
    bi_encoder_rerank_pairs,
    bi_encoder_score,
    cosine_similarity,
    cross_encoder_full_corpus_pairs,
    cross_encoder_score,
    rerank_pair_reduction,
)


def test_cosine_similarity_matches_expected_value() -> None:
    score = cosine_similarity([1.0, 2.0], [2.0, 1.0])
    assert score == pytest.approx(0.8)


def test_cosine_similarity_requires_same_length() -> None:
    with pytest.raises(ValueError, match="same length"):
        cosine_similarity([1.0], [1.0, 2.0])


def test_bi_encoder_score_returns_zero_for_zero_norm_vector() -> None:
    assert bi_encoder_score([1.0, 0.0], [0.0, 0.0]) == 0.0


def test_cross_encoder_score_rewards_ordered_query_document_match() -> None:
    ordered = cross_encoder_score(
        ["refund", "policy"],
        ["refund", "policy", "approved"],
    )
    unordered = cross_encoder_score(
        ["refund", "policy"],
        ["policy", "refund", "approved"],
    )

    assert ordered == pytest.approx(1.0)
    assert unordered == pytest.approx(0.7)
    assert ordered > unordered


def test_cross_encoder_score_returns_zero_for_empty_pair() -> None:
    assert cross_encoder_score([], ["refund"]) == 0.0
    assert cross_encoder_score(["refund"], []) == 0.0


def test_pair_count_helpers_show_reranking_savings() -> None:
    assert cross_encoder_full_corpus_pairs(num_queries=100, corpus_size=1_000) == 100_000
    assert bi_encoder_rerank_pairs(num_queries=100, candidate_k=50) == 5_000
    assert rerank_pair_reduction(corpus_size=1_000, candidate_k=50) == pytest.approx(0.95)


def test_rerank_pair_reduction_requires_candidate_k_within_corpus() -> None:
    with pytest.raises(ValueError, match="cannot exceed"):
        rerank_pair_reduction(corpus_size=100, candidate_k=101)

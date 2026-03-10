import pytest

from retrieval_metrics import (
    reciprocal_rank,
    rerank_disagreement_rate,
    rerank_gain,
    reranker_metrics,
    retrieval_f1_at_k,
    retrieval_hit_rate_at_k,
    retrieval_precision_at_k,
    retrieval_recall_at_k,
)


def test_retrieval_top_k_metrics_cover_precision_recall_and_f1() -> None:
    retrieved = ["a", "b", "c"]
    relevant = {"b", "d"}

    assert retrieval_precision_at_k(retrieved, relevant, k=2) == pytest.approx(0.5)
    assert retrieval_recall_at_k(retrieved, relevant, k=2) == pytest.approx(0.5)
    assert retrieval_f1_at_k(retrieved, relevant, k=2) == pytest.approx(0.5)


def test_hit_rate_counts_query_successes() -> None:
    hit_rate = retrieval_hit_rate_at_k(
        query_retrievals=[["a", "b"], ["x", "y"]],
        query_relevants=[{"b"}, {"z"}],
        k=2,
    )
    assert hit_rate == pytest.approx(0.5)


def test_reciprocal_rank_and_rerank_gain_focus_on_first_hit() -> None:
    assert reciprocal_rank([0, 0, 1]) == pytest.approx(1 / 3)
    assert rerank_gain([0, 0, 1], [1, 0, 0]) == pytest.approx(2 / 3)


def test_reranker_metrics_and_disagreement_rate_capture_quality_and_change() -> None:
    mrr, recall = reranker_metrics([0, 1, 0, 1], k=3)

    assert mrr == pytest.approx(0.5)
    assert recall == pytest.approx(0.5)
    assert rerank_disagreement_rate(["a", "b", "c"], ["a", "c", "b"]) == pytest.approx(2 / 3)


def test_invalid_inputs_raise() -> None:
    with pytest.raises(ValueError, match="positive"):
        retrieval_precision_at_k(["a"], {"a"}, k=0)

    with pytest.raises(ValueError, match="binary"):
        reciprocal_rank([2])

    with pytest.raises(ValueError, match="same length"):
        rerank_disagreement_rate(["a"], ["a", "b"])

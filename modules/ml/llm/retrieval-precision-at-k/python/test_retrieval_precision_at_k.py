import pytest

from retrieval_precision_at_k import retrieval_precision_at_k


def test_retrieval_precision_at_k_counts_relevant_hits_in_top_k() -> None:
    score = retrieval_precision_at_k(
        retrieved_ids=["d1", "d2", "d3", "d4"],
        relevant_ids={"d2", "d4"},
        k=3,
    )

    assert score == pytest.approx(1.0 / 3.0)


def test_retrieval_precision_at_k_ignores_duplicate_hits() -> None:
    score = retrieval_precision_at_k(
        retrieved_ids=["d2", "d2", "d3"],
        relevant_ids={"d2", "d4"},
        k=3,
    )

    assert score == pytest.approx(1.0 / 3.0)


def test_retrieval_precision_at_k_requires_positive_k() -> None:
    with pytest.raises(ValueError, match="positive"):
        retrieval_precision_at_k(retrieved_ids=["d1"], relevant_ids={"d1"}, k=0)

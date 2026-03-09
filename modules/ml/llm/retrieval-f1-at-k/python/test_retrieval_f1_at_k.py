import pytest

from retrieval_f1_at_k import retrieval_f1_at_k


def test_retrieval_f1_at_k_combines_precision_and_recall() -> None:
    score = retrieval_f1_at_k(
        retrieved_ids=["d1", "d2", "d3", "d4"],
        relevant_ids={"d2", "d4"},
        k=3,
    )

    assert score == pytest.approx(0.4)


def test_retrieval_f1_at_k_is_zero_when_no_relevant_items_are_retrieved() -> None:
    score = retrieval_f1_at_k(
        retrieved_ids=["d1", "d3"],
        relevant_ids={"d2"},
        k=2,
    )

    assert score == pytest.approx(0.0)


def test_retrieval_f1_at_k_requires_positive_k() -> None:
    with pytest.raises(ValueError, match="positive"):
        retrieval_f1_at_k(retrieved_ids=["d1"], relevant_ids={"d1"}, k=0)

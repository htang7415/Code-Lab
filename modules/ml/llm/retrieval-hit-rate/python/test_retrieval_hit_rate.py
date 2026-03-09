import pytest

from retrieval_hit_rate import retrieval_hit_rate_at_k


def test_retrieval_hit_rate_at_k_counts_queries_with_any_hit() -> None:
    score = retrieval_hit_rate_at_k(
        query_retrievals=[["d1", "d2"], ["d3", "d4"], ["d5"]],
        query_relevants=[{"d2"}, {"d9"}, {"d5", "d6"}],
        k=2,
    )

    assert score == pytest.approx(2.0 / 3.0)


def test_retrieval_hit_rate_at_k_returns_zero_for_no_queries() -> None:
    assert retrieval_hit_rate_at_k([], [], k=1) == pytest.approx(0.0)


def test_retrieval_hit_rate_at_k_requires_positive_k() -> None:
    with pytest.raises(ValueError, match="positive"):
        retrieval_hit_rate_at_k([["d1"]], [{"d1"}], k=0)

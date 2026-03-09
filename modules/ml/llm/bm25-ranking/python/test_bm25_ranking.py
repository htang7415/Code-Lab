import pytest

from bm25_ranking import bm25_score


def test_bm25_score_matches_standard_formula() -> None:
    score = bm25_score(
        query_terms=["cat", "sat"],
        document_terms=["cat", "cat", "cat", "sat"],
        document_frequencies={"cat": 4, "sat": 8},
        num_documents=20,
        avg_doc_length=5.0,
    )

    assert score == pytest.approx(3.6964431532126127)


def test_bm25_score_returns_zero_for_empty_query() -> None:
    assert bm25_score([], ["cat"], {"cat": 1}, 10, 2.0) == 0.0


def test_bm25_score_requires_document_frequency_for_query_term() -> None:
    with pytest.raises(ValueError, match="missing document frequency"):
        bm25_score(["cat"], ["cat"], {}, 10, 1.0)

import pytest

from tf_idf import tf_idf_weights


def test_tf_idf_weights_match_term_frequency_times_inverse_document_frequency() -> None:
    weights = tf_idf_weights(
        tokens=["cat", "cat", "sat"],
        document_frequencies={"cat": 5, "sat": 2},
        num_documents=10,
    )

    assert weights["cat"] == pytest.approx(0.46209812037329684)
    assert weights["sat"] == pytest.approx(0.5364793041447)


def test_tf_idf_weights_returns_empty_for_empty_document() -> None:
    assert tf_idf_weights([], {"cat": 1}, 10) == {}


def test_tf_idf_weights_requires_term_document_frequency() -> None:
    with pytest.raises(ValueError, match="missing document frequency"):
        tf_idf_weights(["cat"], {}, 10)

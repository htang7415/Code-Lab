import pytest

from top_k_accuracy import top_k_accuracy


def test_top_k_accuracy_counts_hits_within_first_k_predictions() -> None:
    score = top_k_accuracy(
        predicted_rankings=[[1, 2, 3], [3, 2, 1], [0, 2, 1]],
        labels=[2, 1, 4],
        k=2,
    )

    assert score == pytest.approx(1.0 / 3.0)


def test_top_k_accuracy_reduces_to_standard_accuracy_when_k_is_one() -> None:
    score = top_k_accuracy(
        predicted_rankings=[[1, 2], [2, 1]],
        labels=[1, 1],
        k=1,
    )

    assert score == pytest.approx(0.5)


def test_top_k_accuracy_requires_positive_k() -> None:
    with pytest.raises(ValueError, match="positive"):
        top_k_accuracy(predicted_rankings=[[1]], labels=[1], k=0)

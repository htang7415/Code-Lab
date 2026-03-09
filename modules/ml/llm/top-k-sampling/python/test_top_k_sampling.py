import pytest

from top_k_sampling import top_k_filter


def test_top_k_filter_keeps_highest_probability_indices() -> None:
    kept = top_k_filter([0.1, 0.4, 0.3, 0.2], k=2)

    assert kept == [1, 2]


def test_top_k_filter_keeps_all_indices_when_k_is_large() -> None:
    kept = top_k_filter([0.2, 0.5], k=5)

    assert kept == [1, 0]


def test_top_k_filter_requires_positive_k() -> None:
    with pytest.raises(ValueError, match="positive"):
        top_k_filter([1.0], k=0)

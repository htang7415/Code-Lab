import pytest

from top_p_sampling import top_p_filter


def test_top_p_filter_keeps_smallest_prefix_reaching_threshold() -> None:
    kept = top_p_filter([0.4, 0.3, 0.2, 0.1], p=0.6)

    assert kept == [0, 1]


def test_top_p_filter_keeps_all_tokens_for_p_one() -> None:
    kept = top_p_filter([0.2, 0.5, 0.3], p=1.0)

    assert kept == [1, 2, 0]


def test_top_p_filter_requires_valid_threshold() -> None:
    with pytest.raises(ValueError, match="0 < p <= 1"):
        top_p_filter([1.0], p=0.0)

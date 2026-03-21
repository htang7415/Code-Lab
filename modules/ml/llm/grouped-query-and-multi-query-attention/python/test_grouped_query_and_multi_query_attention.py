import pytest

from grouped_query_and_multi_query_attention import (
    kv_cache_fraction,
    kv_cache_reduction_ratio,
    kv_heads_for_layout,
    queries_per_kv_head,
)


def test_kv_heads_for_layout_covers_mha_mqa_and_gqa() -> None:
    assert kv_heads_for_layout(num_query_heads=16, layout="mha") == 16
    assert kv_heads_for_layout(num_query_heads=16, layout="mqa") == 1
    assert kv_heads_for_layout(num_query_heads=16, layout="gqa", grouped_kv_heads=4) == 4


def test_queries_per_kv_head_and_cache_ratios() -> None:
    assert queries_per_kv_head(num_query_heads=16, num_kv_heads=4) == 4
    assert kv_cache_fraction(num_query_heads=16, num_kv_heads=4) == pytest.approx(0.25)
    assert kv_cache_reduction_ratio(num_query_heads=16, num_kv_heads=4) == pytest.approx(0.75)


def test_grouped_query_layout_validates_counts() -> None:
    with pytest.raises(ValueError, match="required"):
        kv_heads_for_layout(num_query_heads=16, layout="gqa")
    with pytest.raises(ValueError, match="divisible"):
        queries_per_kv_head(num_query_heads=10, num_kv_heads=4)
    with pytest.raises(ValueError, match="one of"):
        kv_heads_for_layout(num_query_heads=16, layout="bad")

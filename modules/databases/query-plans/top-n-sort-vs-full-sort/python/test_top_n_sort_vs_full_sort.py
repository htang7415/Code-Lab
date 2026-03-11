from top_n_sort_vs_full_sort import (
    choose_sort_strategy,
    full_sort_work_units,
    sort_strategy_summary,
    top_n_heap_work_units,
)


def test_small_limit_prefers_top_n_heap_over_full_sort():
    full_sort = full_sort_work_units(100_000)
    top_n = top_n_heap_work_units(100_000, 20)

    assert top_n < full_sort
    assert choose_sort_strategy(100_000, 20, has_ordered_index=False) == "top-n-heap"


def test_large_limit_degenerates_to_full_sort():
    summary = sort_strategy_summary(100_000, 80_000, has_ordered_index=False)

    assert summary["strategy"] == "top-n-heap"
    assert float(summary["saved_work"]) < float(summary["full_sort_work"]) * 0.2


def test_ordered_index_avoids_explicit_sort_choice():
    assert choose_sort_strategy(100_000, 20, has_ordered_index=True) == "index-order-scan"

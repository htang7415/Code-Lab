"""top_n_sort_vs_full_sort - compare full sorts with heap-based top-N selection."""

from __future__ import annotations

import math


def full_sort_work_units(row_count: int) -> float:
    if row_count <= 1:
        return 0.0
    return row_count * math.log2(row_count)


def top_n_heap_work_units(row_count: int, limit: int) -> float:
    if row_count <= 0 or limit <= 0 or limit >= row_count:
        return full_sort_work_units(row_count)
    return row_count * math.log2(limit)


def choose_sort_strategy(
    row_count: int,
    limit: int,
    has_ordered_index: bool,
) -> str:
    if has_ordered_index:
        return "index-order-scan"
    if limit <= 0 or limit >= row_count:
        return "full-sort"
    if top_n_heap_work_units(row_count, limit) < full_sort_work_units(row_count):
        return "top-n-heap"
    return "full-sort"


def sort_strategy_summary(
    row_count: int,
    limit: int,
    has_ordered_index: bool,
) -> dict[str, float | str]:
    full_sort = full_sort_work_units(row_count)
    top_n = top_n_heap_work_units(row_count, limit)
    strategy = choose_sort_strategy(row_count, limit, has_ordered_index)
    return {
        "strategy": strategy,
        "full_sort_work": full_sort,
        "top_n_work": top_n,
        "saved_work": 0.0 if strategy == "index-order-scan" else max(full_sort - top_n, 0.0),
    }

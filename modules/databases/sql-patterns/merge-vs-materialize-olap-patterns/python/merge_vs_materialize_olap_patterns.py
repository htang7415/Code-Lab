"""merge_vs_materialize_olap_patterns - compare merge-on-read with materialized summaries."""

from __future__ import annotations


def merge_query_work(base_rows: int, delta_rows: int) -> int:
    return max(base_rows, 0) + max(delta_rows, 0)


def merge_total_work(base_rows: int, delta_rows: int, query_count: int) -> int:
    return merge_query_work(base_rows, delta_rows) * max(query_count, 0)


def materialize_refresh_work(delta_rows: int) -> int:
    return 10_000 + max(delta_rows, 0) * 10


def materialize_total_work(delta_rows: int, query_count: int) -> int:
    return materialize_refresh_work(delta_rows) + max(query_count, 0)


def choose_olap_pattern(base_rows: int, delta_rows: int, query_count: int) -> str:
    return (
        "materialize"
        if materialize_total_work(delta_rows, query_count)
        < merge_total_work(base_rows, delta_rows, query_count)
        else "merge"
    )


def work_summary(base_rows: int, delta_rows: int, query_count: int) -> dict[str, int | str]:
    merge_work = merge_total_work(base_rows, delta_rows, query_count)
    materialize_work = materialize_total_work(delta_rows, query_count)
    return {
        "merge_work": merge_work,
        "materialize_work": materialize_work,
        "choice": choose_olap_pattern(base_rows, delta_rows, query_count),
    }

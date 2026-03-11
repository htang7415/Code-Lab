"""covering_index_vs_table_lookups - compare index-only reads to extra heap fetches."""

from __future__ import annotations


def index_probe_work(index_height: int) -> int:
    return max(index_height, 0) + 1


def table_lookup_work(result_rows: int, covering: bool) -> int:
    if covering:
        return 0
    return max(result_rows, 0)


def total_lookup_work(index_height: int, result_rows: int, covering: bool) -> int:
    return index_probe_work(index_height) + table_lookup_work(result_rows, covering)


def lookup_summary(index_height: int, result_rows: int) -> dict[str, int]:
    covering_work = total_lookup_work(index_height, result_rows, True)
    non_covering_work = total_lookup_work(index_height, result_rows, False)
    return {
        "covering_work": covering_work,
        "non_covering_work": non_covering_work,
        "table_lookups_avoided": max(result_rows, 0),
        "extra_work_without_covering": non_covering_work - covering_work,
    }

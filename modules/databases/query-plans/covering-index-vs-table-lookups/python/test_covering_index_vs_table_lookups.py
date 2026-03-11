from covering_index_vs_table_lookups import (
    lookup_summary,
    table_lookup_work,
    total_lookup_work,
)


def test_covering_index_avoids_table_fetches() -> None:
    assert table_lookup_work(result_rows=5, covering=True) == 0
    assert table_lookup_work(result_rows=5, covering=False) == 5


def test_non_covering_work_grows_with_result_rows() -> None:
    small = total_lookup_work(index_height=3, result_rows=2, covering=False)
    large = total_lookup_work(index_height=3, result_rows=20, covering=False)

    assert small == 6
    assert large == 24


def test_lookup_summary_reports_saved_table_work() -> None:
    summary = lookup_summary(index_height=4, result_rows=8)

    assert summary["covering_work"] == 5
    assert summary["non_covering_work"] == 13
    assert summary["table_lookups_avoided"] == 8
    assert summary["extra_work_without_covering"] == 8

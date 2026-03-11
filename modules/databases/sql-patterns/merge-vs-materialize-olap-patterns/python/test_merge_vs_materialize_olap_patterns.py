from merge_vs_materialize_olap_patterns import (
    choose_olap_pattern,
    materialize_total_work,
    merge_total_work,
    work_summary,
)


def test_many_repeated_queries_favor_materialized_summary():
    assert choose_olap_pattern(base_rows=1_000_000, delta_rows=50_000, query_count=20) == "materialize"
    assert materialize_total_work(50_000, 20) < merge_total_work(1_000_000, 50_000, 20)


def test_single_query_can_leave_merge_on_read_cheaper():
    summary = work_summary(base_rows=10_000, delta_rows=100, query_count=1)

    assert summary["choice"] == "merge"
    assert int(summary["merge_work"]) < int(summary["materialize_work"])

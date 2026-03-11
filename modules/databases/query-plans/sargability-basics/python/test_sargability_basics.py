from sargability_basics import (
    add_created_day_index,
    count_rows_for_month,
    count_rows_in_range,
    create_connection,
    create_event_table,
    nonsargable_month_plan,
    plan_summary,
    seed_events,
    sargable_range_plan,
)


def test_raw_range_predicate_is_searchable_but_wrapped_column_is_not() -> None:
    conn = create_connection()
    create_event_table(conn)
    seed_events(
        conn,
        [
            "2026-01-01",
            "2026-01-10",
            "2026-01-20",
            "2026-02-01",
            "2026-02-14",
        ],
    )
    add_created_day_index(conn)

    sargable = plan_summary(sargable_range_plan(conn, "2026-01-01", "2026-02-01"))
    nonsargable = plan_summary(nonsargable_month_plan(conn, "2026-01"))

    assert sargable["uses_index_search"] is True
    assert nonsargable["uses_index_search"] is False
    assert nonsargable["uses_scan"] is True


def test_range_rewrite_keeps_the_same_january_result_set() -> None:
    conn = create_connection()
    create_event_table(conn)
    seed_events(
        conn,
        [
            "2026-01-01",
            "2026-01-10",
            "2026-01-20",
            "2026-02-01",
            "2026-02-14",
        ],
    )
    add_created_day_index(conn)

    assert count_rows_in_range(conn, "2026-01-01", "2026-02-01") == 3
    assert count_rows_for_month(conn, "2026-01") == 3

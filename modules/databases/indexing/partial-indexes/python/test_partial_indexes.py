from partial_indexes import (
    add_failed_runs_partial_index,
    create_connection,
    create_eval_runs_table,
    plan_flags,
    plan_for_recent_completed_runs,
    plan_for_recent_failed_runs,
    seed_eval_runs,
)


def build_seeded_connection():
    conn = create_connection()
    create_eval_runs_table(conn)
    seed_eval_runs(
        conn,
        [
            (7, "queued", "2026-03-01T08:00:00Z"),
            (7, "failed", "2026-03-02T08:00:00Z"),
            (7, "completed", "2026-03-03T08:00:00Z"),
            (8, "failed", "2026-03-04T08:00:00Z"),
            (7, "failed", "2026-03-05T08:00:00Z"),
        ],
    )
    return conn


def test_failed_query_starts_as_a_scan_before_partial_indexing() -> None:
    conn = build_seeded_connection()

    assert plan_flags(plan_for_recent_failed_runs(conn, 7)) == {
        "full_scan": True,
        "uses_partial_index": False,
        "temp_sort": True,
    }


def test_failed_query_uses_the_partial_index_after_it_is_added() -> None:
    conn = build_seeded_connection()
    add_failed_runs_partial_index(conn)

    assert plan_flags(plan_for_recent_failed_runs(conn, 7)) == {
        "full_scan": False,
        "uses_partial_index": True,
        "temp_sort": False,
    }


def test_completed_query_cannot_use_the_failed_only_partial_index() -> None:
    conn = build_seeded_connection()
    add_failed_runs_partial_index(conn)

    assert plan_flags(plan_for_recent_completed_runs(conn, 7)) == {
        "full_scan": True,
        "uses_partial_index": False,
        "temp_sort": True,
    }

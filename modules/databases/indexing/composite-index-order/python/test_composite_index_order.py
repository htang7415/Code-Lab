from composite_index_order import (
    add_bad_index_status_workspace_created,
    add_good_index_workspace_created,
    create_connection,
    create_runs_table,
    plan_flags,
    plan_for_workspace_recent_runs,
    recent_runs_for_workspace,
    seed_runs,
)


def build_seeded_connection():
    conn = create_connection()
    create_runs_table(conn)
    seed_runs(
        conn,
        [
            (7, "queued", "2026-03-01T08:00:00Z"),
            (7, "completed", "2026-03-02T08:00:00Z"),
            (8, "completed", "2026-03-03T08:00:00Z"),
            (7, "failed", "2026-03-04T08:00:00Z"),
            (7, "completed", "2026-03-05T08:00:00Z"),
        ],
    )
    return conn


def test_bad_index_order_does_not_help_a_workspace_only_query() -> None:
    conn = build_seeded_connection()
    add_bad_index_status_workspace_created(conn)

    assert plan_flags(plan_for_workspace_recent_runs(conn, workspace_id=7)) == {
        "full_scan": True,
        "uses_bad_index": False,
        "uses_good_index": False,
        "temp_sort": True,
    }


def test_good_index_order_matches_the_query_prefix_and_sort_order() -> None:
    conn = build_seeded_connection()
    add_good_index_workspace_created(conn)

    assert plan_flags(plan_for_workspace_recent_runs(conn, workspace_id=7)) == {
        "full_scan": False,
        "uses_bad_index": False,
        "uses_good_index": True,
        "temp_sort": False,
    }


def test_good_index_changes_the_plan_but_not_the_query_result() -> None:
    conn = build_seeded_connection()
    before = recent_runs_for_workspace(conn, workspace_id=7)
    add_good_index_workspace_created(conn)
    after = recent_runs_for_workspace(conn, workspace_id=7)

    assert before == after == [
        (5, "2026-03-05T08:00:00Z"),
        (4, "2026-03-04T08:00:00Z"),
    ]

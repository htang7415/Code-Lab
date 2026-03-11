from btree_basics import (
    add_workspace_status_created_index,
    create_connection,
    create_eval_runs_table,
    plan_for_recent_completed_runs,
    recent_completed_runs,
    seed_eval_runs,
)


def build_seeded_connection():
    conn = create_connection()
    create_eval_runs_table(conn)
    seed_eval_runs(
        conn,
        [
            (7, "queued", "2026-03-01T08:00:00Z", 180),
            (7, "completed", "2026-03-01T09:00:00Z", 125),
            (7, "completed", "2026-03-02T09:00:00Z", 118),
            (7, "failed", "2026-03-03T09:00:00Z", 90),
            (8, "completed", "2026-03-04T09:00:00Z", 100),
            (7, "completed", "2026-03-05T09:00:00Z", 111),
        ],
    )
    return conn


def test_query_plan_starts_with_a_full_scan_before_the_index_exists() -> None:
    conn = build_seeded_connection()
    plan = plan_for_recent_completed_runs(conn, workspace_id=7)

    assert any("SCAN eval_runs" in detail for detail in plan)


def test_query_plan_mentions_the_composite_index_after_creation() -> None:
    conn = build_seeded_connection()
    add_workspace_status_created_index(conn)
    plan = plan_for_recent_completed_runs(conn, workspace_id=7)

    assert any(
        "idx_eval_runs_workspace_status_created" in detail for detail in plan
    )
    assert all("SCAN eval_runs" not in detail for detail in plan)


def test_recent_completed_runs_follow_the_same_results_with_or_without_index() -> None:
    conn = build_seeded_connection()
    before = recent_completed_runs(conn, workspace_id=7)

    add_workspace_status_created_index(conn)
    after = recent_completed_runs(conn, workspace_id=7)

    assert before == after == [
        (6, "2026-03-05T09:00:00Z"),
        (3, "2026-03-02T09:00:00Z"),
        (2, "2026-03-01T09:00:00Z"),
    ]

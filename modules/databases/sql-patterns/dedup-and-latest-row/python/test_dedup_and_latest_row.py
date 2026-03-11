from dedup_and_latest_row import (
    create_connection,
    create_run_events_table,
    latest_event_per_run,
    latest_status_summary,
    record_run_event,
)


def build_seeded_connection():
    conn = create_connection()
    create_run_events_table(conn)
    record_run_event(conn, "run-1", "queued", "2026-03-10T09:00:00Z")
    record_run_event(conn, "run-1", "running", "2026-03-10T09:02:00Z")
    record_run_event(conn, "run-1", "completed", "2026-03-10T09:05:00Z")
    record_run_event(conn, "run-2", "queued", "2026-03-10T09:01:00Z")
    record_run_event(conn, "run-2", "failed", "2026-03-10T09:06:00Z")
    return conn


def test_latest_event_per_run_keeps_only_the_newest_row_for_each_run() -> None:
    conn = build_seeded_connection()

    assert latest_event_per_run(conn) == [
        {
            "run_id": "run-1",
            "status": "completed",
            "recorded_at": "2026-03-10T09:05:00Z",
        },
        {
            "run_id": "run-2",
            "status": "failed",
            "recorded_at": "2026-03-10T09:06:00Z",
        },
    ]


def test_equal_timestamps_use_the_later_inserted_row_as_a_tie_breaker() -> None:
    conn = create_connection()
    create_run_events_table(conn)
    record_run_event(conn, "run-1", "running", "2026-03-10T09:00:00Z")
    record_run_event(conn, "run-1", "completed", "2026-03-10T09:00:00Z")

    assert latest_event_per_run(conn) == [
        {
            "run_id": "run-1",
            "status": "completed",
            "recorded_at": "2026-03-10T09:00:00Z",
        }
    ]


def test_summary_counts_latest_statuses_after_deduplication() -> None:
    conn = build_seeded_connection()

    assert latest_status_summary(conn) == {
        "completed": 1,
        "failed": 1,
    }

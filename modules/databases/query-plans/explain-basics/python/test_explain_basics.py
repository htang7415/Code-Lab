from explain_basics import (
    add_recent_events_index,
    create_connection,
    create_events_table,
    explain_recent_workspace_events,
    plan_flags,
    recent_workspace_events,
    seed_events,
)


def build_seeded_connection():
    conn = create_connection()
    create_events_table(conn)
    seed_events(
        conn,
        [
            (7, "2026-03-01T08:00:00Z", "ingest.started"),
            (7, "2026-03-02T08:00:00Z", "ingest.finished"),
            (8, "2026-03-02T09:00:00Z", "ingest.finished"),
            (7, "2026-03-03T08:00:00Z", "embed.started"),
            (7, "2026-03-04T08:00:00Z", "embed.finished"),
        ],
    )
    return conn


def test_plan_flags_detect_a_full_scan_and_temp_sort_before_indexing() -> None:
    conn = build_seeded_connection()

    flags = plan_flags(explain_recent_workspace_events(conn, workspace_id=7))

    assert flags == {
        "full_scan": True,
        "uses_index": False,
        "temp_sort": True,
    }


def test_plan_flags_show_index_usage_after_adding_the_composite_index() -> None:
    conn = build_seeded_connection()
    add_recent_events_index(conn)

    flags = plan_flags(explain_recent_workspace_events(conn, workspace_id=7))

    assert flags == {
        "full_scan": False,
        "uses_index": True,
        "temp_sort": False,
    }


def test_index_does_not_change_the_query_result() -> None:
    conn = build_seeded_connection()
    before = recent_workspace_events(conn, workspace_id=7)

    add_recent_events_index(conn)
    after = recent_workspace_events(conn, workspace_id=7)

    assert before == after == [
        (5, "2026-03-04T08:00:00Z"),
        (4, "2026-03-03T08:00:00Z"),
    ]

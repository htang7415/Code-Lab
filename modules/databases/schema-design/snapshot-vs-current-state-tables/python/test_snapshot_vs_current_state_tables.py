from snapshot_vs_current_state_tables import (
    capture_prompt_snapshot,
    create_connection,
    create_snapshot_schema,
    current_prompt_models,
    snapshot_history,
    snapshot_model_as_of,
    upsert_current_config,
)


def test_current_state_table_keeps_only_the_latest_model() -> None:
    conn = create_connection()
    create_snapshot_schema(conn)

    upsert_current_config(conn, "retrieval-answer", "gpt-4.1-mini", "2026-01-01")
    upsert_current_config(conn, "retrieval-answer", "gpt-5-small", "2026-02-01")

    assert current_prompt_models(conn) == {"retrieval-answer": "gpt-5-small"}


def test_snapshot_table_supports_point_in_time_reads() -> None:
    conn = create_connection()
    create_snapshot_schema(conn)

    capture_prompt_snapshot(conn, "retrieval-answer", "gpt-4.1-mini", "2026-01-01")
    capture_prompt_snapshot(conn, "retrieval-answer", "gpt-5-small", "2026-02-01")

    assert snapshot_history(conn, "retrieval-answer") == [
        ("2026-01-01", "gpt-4.1-mini"),
        ("2026-02-01", "gpt-5-small"),
    ]
    assert snapshot_model_as_of(conn, "retrieval-answer", "2026-01-15") == "gpt-4.1-mini"
    assert snapshot_model_as_of(conn, "retrieval-answer", "2026-02-15") == "gpt-5-small"

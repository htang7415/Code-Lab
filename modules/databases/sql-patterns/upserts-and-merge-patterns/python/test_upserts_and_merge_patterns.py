from upserts_and_merge_patterns import (
    create_connection,
    create_model_scores_table,
    merge_score_batch,
    score_rows,
    upsert_score,
)


def test_upsert_inserts_new_rows_and_updates_existing_keys() -> None:
    conn = create_connection()
    create_model_scores_table(conn)
    upsert_score(conn, "gpt-mini", "helpfulness", 0.81, "2026-03-10T09:00:00Z")
    upsert_score(conn, "gpt-mini", "helpfulness", 0.84, "2026-03-11T09:00:00Z")

    assert score_rows(conn) == [
        ("gpt-mini", "helpfulness", 0.84, "2026-03-11T09:00:00Z"),
    ]


def test_stale_upsert_does_not_overwrite_a_newer_row() -> None:
    conn = create_connection()
    create_model_scores_table(conn)
    upsert_score(conn, "gpt-mini", "helpfulness", 0.84, "2026-03-11T09:00:00Z")
    upsert_score(conn, "gpt-mini", "helpfulness", 0.80, "2026-03-10T09:00:00Z")

    assert score_rows(conn) == [
        ("gpt-mini", "helpfulness", 0.84, "2026-03-11T09:00:00Z"),
    ]


def test_batch_merge_handles_multiple_business_keys() -> None:
    conn = create_connection()
    create_model_scores_table(conn)
    merge_score_batch(
        conn,
        [
            ("gpt-mini", "helpfulness", 0.84, "2026-03-11T09:00:00Z"),
            ("gpt-mini", "grounding", 0.79, "2026-03-11T09:00:00Z"),
            ("rag-large", "helpfulness", 0.88, "2026-03-11T09:05:00Z"),
        ],
    )

    assert score_rows(conn) == [
        ("gpt-mini", "grounding", 0.79, "2026-03-11T09:00:00Z"),
        ("gpt-mini", "helpfulness", 0.84, "2026-03-11T09:00:00Z"),
        ("rag-large", "helpfulness", 0.88, "2026-03-11T09:05:00Z"),
    ]

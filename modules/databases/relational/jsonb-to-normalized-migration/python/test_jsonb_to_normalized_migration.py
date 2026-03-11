from jsonb_to_normalized_migration import (
    backfill_ticket_tags,
    create_connection,
    create_legacy_schema,
    create_normalized_tag_table,
    insert_legacy_ticket,
    tag_rows,
    tickets_with_tag_from_json,
    tickets_with_tag_from_normalized,
)


def test_backfill_preserves_query_results_for_hot_tag_filters():
    conn = create_connection()
    create_legacy_schema(conn)
    wanted_id = insert_legacy_ticket(
        conn,
        workspace_id=7,
        title="Broken retrieval",
        metadata={"priority": "high", "tags": ["rag", "prod"]},
    )
    insert_legacy_ticket(
        conn,
        workspace_id=7,
        title="Warm cache",
        metadata={"priority": "low", "tags": ["cache"]},
    )
    insert_legacy_ticket(
        conn,
        workspace_id=8,
        title="Other tenant",
        metadata={"priority": "high", "tags": ["rag"]},
    )

    create_normalized_tag_table(conn)
    backfill_ticket_tags(conn)

    assert tickets_with_tag_from_json(conn, 7, "rag") == [wanted_id]
    assert tickets_with_tag_from_normalized(conn, 7, "rag") == [wanted_id]


def test_backfill_is_idempotent_and_deduplicates_tags():
    conn = create_connection()
    create_legacy_schema(conn)
    ticket_id = insert_legacy_ticket(
        conn,
        workspace_id=7,
        title="Duplicate tags",
        metadata={"tags": ["rag", "rag", "prod"]},
    )
    create_normalized_tag_table(conn)

    backfill_ticket_tags(conn)
    backfill_ticket_tags(conn)

    assert tag_rows(conn) == [(ticket_id, "prod"), (ticket_id, "rag")]

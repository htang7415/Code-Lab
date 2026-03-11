from optimistic_concurrency_control import (
    create_connection,
    create_document_table,
    insert_document,
    read_document,
    update_document_if_version,
)


def test_version_checked_update_succeeds_for_current_reader() -> None:
    conn = create_connection()
    create_document_table(conn)
    document_id = insert_document(conn, "Runbook", "draft")

    assert update_document_if_version(conn, document_id, expected_version=1, new_status="review") is True
    assert read_document(conn, document_id) == {
        "id": document_id,
        "title": "Runbook",
        "status": "review",
        "version": 2,
    }


def test_stale_writer_fails_until_it_reloads_the_version() -> None:
    conn = create_connection()
    create_document_table(conn)
    document_id = insert_document(conn, "Prompt", "draft")

    assert update_document_if_version(conn, document_id, expected_version=1, new_status="review") is True
    assert update_document_if_version(conn, document_id, expected_version=1, new_status="published") is False
    assert read_document(conn, document_id)["status"] == "review"

    assert update_document_if_version(conn, document_id, expected_version=2, new_status="published") is True
    assert read_document(conn, document_id)["version"] == 3

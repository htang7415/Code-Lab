import sqlite3

import pytest

from constraints_and_integrity import (
    create_connection,
    create_integrity_schema,
    document_rows,
    insert_document,
    insert_workspace,
)


def build_seeded_connection():
    conn = create_connection()
    create_integrity_schema(conn)
    workspace_id = insert_workspace(conn, "research")
    return conn, workspace_id


def test_same_title_is_unique_within_one_workspace_but_not_globally() -> None:
    conn, workspace_id = build_seeded_connection()
    other_workspace_id = insert_workspace(conn, "production")
    insert_document(conn, workspace_id, "spec", "draft")
    insert_document(conn, other_workspace_id, "spec", "published")

    with pytest.raises(sqlite3.IntegrityError):
        insert_document(conn, workspace_id, "spec", "archived")

    assert document_rows(conn) == [
        ("research", "spec", "draft"),
        ("production", "spec", "published"),
    ]


def test_check_constraint_rejects_invalid_status_values() -> None:
    conn, workspace_id = build_seeded_connection()

    with pytest.raises(sqlite3.IntegrityError):
        insert_document(conn, workspace_id, "spec", "running")


def test_foreign_key_and_not_null_constraints_block_invalid_rows() -> None:
    conn, workspace_id = build_seeded_connection()

    with pytest.raises(sqlite3.IntegrityError):
        insert_document(conn, 999, "spec", "draft")

    with pytest.raises(sqlite3.IntegrityError):
        insert_document(conn, workspace_id, None, "draft")  # type: ignore[arg-type]

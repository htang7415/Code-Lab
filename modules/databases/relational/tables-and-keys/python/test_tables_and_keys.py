import sqlite3

import pytest

from tables_and_keys import (
    chunk_counts_by_document,
    create_connection,
    create_core_tables,
    insert_chunk,
    insert_document,
    insert_workspace,
)


def test_foreign_key_blocks_orphan_chunks() -> None:
    conn = create_connection()
    create_core_tables(conn)

    with pytest.raises(sqlite3.IntegrityError):
        insert_chunk(conn, document_id=999, chunk_index=0, text="orphan")


def test_chunk_index_is_unique_within_a_document() -> None:
    conn = create_connection()
    create_core_tables(conn)
    workspace_id = insert_workspace(conn, "research")
    document_id = insert_document(conn, workspace_id, "rag-notes")

    insert_chunk(conn, document_id, 0, "first chunk")

    with pytest.raises(sqlite3.IntegrityError):
        insert_chunk(conn, document_id, 0, "duplicate chunk index")


def test_left_join_keeps_documents_without_chunks() -> None:
    conn = create_connection()
    create_core_tables(conn)
    workspace_id = insert_workspace(conn, "research")
    with_chunks = insert_document(conn, workspace_id, "rag-notes")
    insert_document(conn, workspace_id, "roadmap")

    insert_chunk(conn, with_chunks, 0, "chunk zero")
    insert_chunk(conn, with_chunks, 1, "chunk one")

    assert chunk_counts_by_document(conn) == [
        ("research", "rag-notes", 2),
        ("research", "roadmap", 0),
    ]

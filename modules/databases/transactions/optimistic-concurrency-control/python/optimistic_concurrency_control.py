"""optimistic_concurrency_control - compare-and-swap updates with version checks."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_document_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT NOT NULL,
            version INTEGER NOT NULL
        )
        """
    )


def insert_document(conn: sqlite3.Connection, title: str, status: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO documents (title, status, version)
        VALUES (?, ?, 1)
        """,
        (title, status),
    )
    return int(cursor.lastrowid)


def read_document(conn: sqlite3.Connection, document_id: int) -> dict[str, object]:
    row = conn.execute(
        """
        SELECT id, title, status, version
        FROM documents
        WHERE id = ?
        """,
        (document_id,),
    ).fetchone()
    if row is None:
        raise ValueError(f"missing document {document_id}")
    return {
        "id": int(row[0]),
        "title": str(row[1]),
        "status": str(row[2]),
        "version": int(row[3]),
    }


def update_document_if_version(
    conn: sqlite3.Connection,
    document_id: int,
    expected_version: int,
    new_status: str,
) -> bool:
    cursor = conn.execute(
        """
        UPDATE documents
        SET status = ?, version = version + 1
        WHERE id = ? AND version = ?
        """,
        (new_status, document_id, expected_version),
    )
    return cursor.rowcount == 1

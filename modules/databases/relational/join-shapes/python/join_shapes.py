"""join_shapes - inner joins, left joins, and anti-joins."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_join_demo_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL
        );

        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL,
            chunk_index INTEGER NOT NULL,
            text TEXT NOT NULL,
            FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE,
            UNIQUE (document_id, chunk_index)
        );
        """
    )


def seed_documents(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
    conn.executemany(
        "INSERT INTO documents (id, title) VALUES (?, ?)",
        rows,
    )


def seed_chunks(
    conn: sqlite3.Connection,
    rows: list[tuple[int, int, str]],
) -> None:
    conn.executemany(
        """
        INSERT INTO chunks (document_id, chunk_index, text)
        VALUES (?, ?, ?)
        """,
        rows,
    )


def inner_join_document_chunks(conn: sqlite3.Connection) -> list[tuple[str, str]]:
    rows = conn.execute(
        """
        SELECT d.title, c.text
        FROM documents AS d
        JOIN chunks AS c ON c.document_id = d.id
        ORDER BY d.id, c.chunk_index
        """
    ).fetchall()
    return [(title, text) for title, text in rows]


def left_join_document_chunk_counts(conn: sqlite3.Connection) -> list[tuple[str, int]]:
    rows = conn.execute(
        """
        SELECT d.title, COUNT(c.id) AS chunk_count
        FROM documents AS d
        LEFT JOIN chunks AS c ON c.document_id = d.id
        GROUP BY d.id, d.title
        ORDER BY d.id
        """
    ).fetchall()
    return [(title, chunk_count) for title, chunk_count in rows]


def documents_without_chunks(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute(
        """
        SELECT d.title
        FROM documents AS d
        LEFT JOIN chunks AS c ON c.document_id = d.id
        WHERE c.id IS NULL
        ORDER BY d.id
        """
    ).fetchall()
    return [title for (title,) in rows]

"""tables_and_keys - primary keys, foreign keys, and join basics."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    """Create an in-memory SQLite database with foreign keys enabled."""
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_core_tables(conn: sqlite3.Connection) -> None:
    """Create a tiny relational schema for workspaces, documents, and chunks."""
    conn.executescript(
        """
        CREATE TABLE workspaces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );

        CREATE TABLE documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            source_uri TEXT,
            FOREIGN KEY (workspace_id) REFERENCES workspaces(id) ON DELETE CASCADE,
            UNIQUE (workspace_id, title)
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


def insert_workspace(conn: sqlite3.Connection, name: str) -> int:
    cursor = conn.execute(
        "INSERT INTO workspaces (name) VALUES (?)",
        (name,),
    )
    return int(cursor.lastrowid)


def insert_document(
    conn: sqlite3.Connection,
    workspace_id: int,
    title: str,
    source_uri: str | None = None,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO documents (workspace_id, title, source_uri)
        VALUES (?, ?, ?)
        """,
        (workspace_id, title, source_uri),
    )
    return int(cursor.lastrowid)


def insert_chunk(
    conn: sqlite3.Connection,
    document_id: int,
    chunk_index: int,
    text: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO chunks (document_id, chunk_index, text)
        VALUES (?, ?, ?)
        """,
        (document_id, chunk_index, text),
    )
    return int(cursor.lastrowid)


def chunk_counts_by_document(conn: sqlite3.Connection) -> list[tuple[str, str, int]]:
    """Return one row per document, even if it has zero chunks."""
    rows = conn.execute(
        """
        SELECT w.name, d.title, COUNT(c.id) AS chunk_count
        FROM documents AS d
        JOIN workspaces AS w ON w.id = d.workspace_id
        LEFT JOIN chunks AS c ON c.document_id = d.id
        GROUP BY d.id, w.name, d.title
        ORDER BY d.id
        """
    ).fetchall()
    return [(workspace, title, chunk_count) for workspace, title, chunk_count in rows]

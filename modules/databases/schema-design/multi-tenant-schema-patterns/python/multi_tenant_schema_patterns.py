"""multi_tenant_schema_patterns - tenant-scoped uniqueness and foreign keys."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_multi_tenant_schema(conn: sqlite3.Connection) -> None:
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
            FOREIGN KEY (workspace_id) REFERENCES workspaces(id) ON DELETE CASCADE,
            UNIQUE (workspace_id, id),
            UNIQUE (workspace_id, title)
        );

        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            document_id INTEGER NOT NULL,
            chunk_index INTEGER NOT NULL,
            text TEXT NOT NULL,
            FOREIGN KEY (workspace_id) REFERENCES workspaces(id) ON DELETE CASCADE,
            FOREIGN KEY (workspace_id, document_id)
                REFERENCES documents(workspace_id, id) ON DELETE CASCADE,
            UNIQUE (workspace_id, document_id, chunk_index)
        );
        """
    )


def insert_workspace(conn: sqlite3.Connection, name: str) -> int:
    cursor = conn.execute(
        "INSERT INTO workspaces (name) VALUES (?)",
        (name,),
    )
    return int(cursor.lastrowid)


def insert_document(conn: sqlite3.Connection, workspace_id: int, title: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO documents (workspace_id, title)
        VALUES (?, ?)
        """,
        (workspace_id, title),
    )
    return int(cursor.lastrowid)


def insert_chunk(
    conn: sqlite3.Connection,
    workspace_id: int,
    document_id: int,
    chunk_index: int,
    text: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO chunks (workspace_id, document_id, chunk_index, text)
        VALUES (?, ?, ?, ?)
        """,
        (workspace_id, document_id, chunk_index, text),
    )
    return int(cursor.lastrowid)


def document_titles_for_workspace(
    conn: sqlite3.Connection,
    workspace_id: int,
) -> list[str]:
    rows = conn.execute(
        """
        SELECT title
        FROM documents
        WHERE workspace_id = ?
        ORDER BY id
        """,
        (workspace_id,),
    ).fetchall()
    return [title for (title,) in rows]

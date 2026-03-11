"""constraints_and_integrity - core schema constraints for relational correctness."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_integrity_schema(conn: sqlite3.Connection) -> None:
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
            status TEXT NOT NULL CHECK (status IN ('draft', 'published', 'archived')),
            FOREIGN KEY (workspace_id) REFERENCES workspaces(id) ON DELETE CASCADE,
            UNIQUE (workspace_id, title)
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
    status: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO documents (workspace_id, title, status)
        VALUES (?, ?, ?)
        """,
        (workspace_id, title, status),
    )
    return int(cursor.lastrowid)


def document_rows(conn: sqlite3.Connection) -> list[tuple[str, str, str]]:
    rows = conn.execute(
        """
        SELECT w.name, d.title, d.status
        FROM documents AS d
        JOIN workspaces AS w ON w.id = d.workspace_id
        ORDER BY w.id, d.id
        """
    ).fetchall()
    return [(workspace, title, status) for workspace, title, status in rows]

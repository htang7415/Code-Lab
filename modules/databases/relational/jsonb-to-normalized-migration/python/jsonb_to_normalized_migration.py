"""jsonb_to_normalized_migration - move hot JSON metadata into relational tables."""

from __future__ import annotations

import json
import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_legacy_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            metadata_json TEXT NOT NULL
        )
        """
    )


def insert_legacy_ticket(
    conn: sqlite3.Connection,
    workspace_id: int,
    title: str,
    metadata: dict[str, object],
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO tickets (workspace_id, title, metadata_json)
        VALUES (?, ?, ?)
        """,
        (workspace_id, title, json.dumps(metadata, sort_keys=True)),
    )
    return int(cursor.lastrowid)


def create_normalized_tag_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE ticket_tags (
            ticket_id INTEGER NOT NULL,
            tag TEXT NOT NULL,
            PRIMARY KEY (ticket_id, tag),
            FOREIGN KEY (ticket_id) REFERENCES tickets (id) ON DELETE CASCADE
        )
        """
    )


def backfill_ticket_tags(conn: sqlite3.Connection) -> None:
    rows = conn.execute(
        """
        SELECT id, metadata_json
        FROM tickets
        ORDER BY id
        """
    ).fetchall()
    for ticket_id, metadata_json in rows:
        metadata = json.loads(str(metadata_json))
        tags = metadata.get("tags", [])
        if not isinstance(tags, list):
            continue
        conn.executemany(
            """
            INSERT OR IGNORE INTO ticket_tags (ticket_id, tag)
            VALUES (?, ?)
            """,
            [(int(ticket_id), str(tag)) for tag in sorted(set(tags))],
        )


def tickets_with_tag_from_json(
    conn: sqlite3.Connection,
    workspace_id: int,
    tag: str,
) -> list[int]:
    rows = conn.execute(
        """
        SELECT id, metadata_json
        FROM tickets
        WHERE workspace_id = ?
        ORDER BY id
        """,
        (workspace_id,),
    ).fetchall()
    matches: list[int] = []
    for ticket_id, metadata_json in rows:
        metadata = json.loads(str(metadata_json))
        tags = metadata.get("tags", [])
        if isinstance(tags, list) and tag in tags:
            matches.append(int(ticket_id))
    return matches


def tickets_with_tag_from_normalized(
    conn: sqlite3.Connection,
    workspace_id: int,
    tag: str,
) -> list[int]:
    rows = conn.execute(
        """
        SELECT t.id
        FROM tickets AS t
        JOIN ticket_tags AS tt
          ON tt.ticket_id = t.id
        WHERE t.workspace_id = ? AND tt.tag = ?
        ORDER BY t.id
        """,
        (workspace_id, tag),
    ).fetchall()
    return [int(ticket_id) for (ticket_id,) in rows]


def tag_rows(conn: sqlite3.Connection) -> list[tuple[int, str]]:
    rows = conn.execute(
        """
        SELECT ticket_id, tag
        FROM ticket_tags
        ORDER BY ticket_id, tag
        """
    ).fetchall()
    return [(int(ticket_id), str(tag)) for ticket_id, tag in rows]

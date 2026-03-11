"""snapshot_vs_current_state_tables - current rows for now, snapshots for history."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_snapshot_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE prompt_configs_current (
            prompt_id TEXT PRIMARY KEY,
            model_name TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE TABLE prompt_config_snapshots (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt_id TEXT NOT NULL,
            model_name TEXT NOT NULL,
            captured_at TEXT NOT NULL
        );
        """
    )


def upsert_current_config(
    conn: sqlite3.Connection,
    prompt_id: str,
    model_name: str,
    updated_at: str,
) -> None:
    conn.execute(
        """
        INSERT INTO prompt_configs_current (prompt_id, model_name, updated_at)
        VALUES (?, ?, ?)
        ON CONFLICT(prompt_id) DO UPDATE SET
            model_name = excluded.model_name,
            updated_at = excluded.updated_at
        """,
        (prompt_id, model_name, updated_at),
    )


def capture_prompt_snapshot(
    conn: sqlite3.Connection,
    prompt_id: str,
    model_name: str,
    captured_at: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO prompt_config_snapshots (prompt_id, model_name, captured_at)
        VALUES (?, ?, ?)
        """,
        (prompt_id, model_name, captured_at),
    )
    return int(cursor.lastrowid)


def current_prompt_models(conn: sqlite3.Connection) -> dict[str, str]:
    rows = conn.execute(
        """
        SELECT prompt_id, model_name
        FROM prompt_configs_current
        ORDER BY prompt_id
        """
    ).fetchall()
    return {prompt_id: model_name for prompt_id, model_name in rows}


def snapshot_model_as_of(
    conn: sqlite3.Connection,
    prompt_id: str,
    as_of: str,
) -> str | None:
    row = conn.execute(
        """
        SELECT model_name
        FROM prompt_config_snapshots
        WHERE prompt_id = ? AND captured_at <= ?
        ORDER BY captured_at DESC, id DESC
        LIMIT 1
        """,
        (prompt_id, as_of),
    ).fetchone()
    if row is None:
        return None
    return str(row[0])


def snapshot_history(conn: sqlite3.Connection, prompt_id: str) -> list[tuple[str, str]]:
    rows = conn.execute(
        """
        SELECT captured_at, model_name
        FROM prompt_config_snapshots
        WHERE prompt_id = ?
        ORDER BY captured_at, id
        """,
        (prompt_id,),
    ).fetchall()
    return [(captured_at, model_name) for captured_at, model_name in rows]

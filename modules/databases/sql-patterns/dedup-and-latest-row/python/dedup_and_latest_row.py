"""dedup_and_latest_row - keep the newest row per run with window functions."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_run_events_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE run_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_id TEXT NOT NULL,
            status TEXT NOT NULL,
            recorded_at TEXT NOT NULL
        )
        """
    )


def record_run_event(
    conn: sqlite3.Connection,
    run_id: str,
    status: str,
    recorded_at: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO run_events (run_id, status, recorded_at)
        VALUES (?, ?, ?)
        """,
        (run_id, status, recorded_at),
    )
    return int(cursor.lastrowid)


def latest_event_per_run(conn: sqlite3.Connection) -> list[dict[str, object]]:
    rows = conn.execute(
        """
        WITH ranked AS (
            SELECT
                run_id,
                status,
                recorded_at,
                ROW_NUMBER() OVER (
                    PARTITION BY run_id
                    ORDER BY recorded_at DESC, id DESC
                ) AS row_rank
            FROM run_events
        )
        SELECT run_id, status, recorded_at
        FROM ranked
        WHERE row_rank = 1
        ORDER BY run_id
        """
    ).fetchall()
    return [
        {"run_id": run_id, "status": status, "recorded_at": recorded_at}
        for run_id, status, recorded_at in rows
    ]


def latest_status_summary(conn: sqlite3.Connection) -> dict[str, int]:
    rows = conn.execute(
        """
        WITH ranked AS (
            SELECT
                run_id,
                status,
                ROW_NUMBER() OVER (
                    PARTITION BY run_id
                    ORDER BY recorded_at DESC, id DESC
                ) AS row_rank
            FROM run_events
        )
        SELECT status, COUNT(*)
        FROM ranked
        WHERE row_rank = 1
        GROUP BY status
        ORDER BY status
        """
    ).fetchall()
    return {status: count for status, count in rows}

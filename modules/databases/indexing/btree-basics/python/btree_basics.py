"""btree_basics - use a composite B-tree index for a hot query path."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_eval_runs_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE eval_runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            latency_ms INTEGER NOT NULL
        )
        """
    )


def seed_eval_runs(
    conn: sqlite3.Connection,
    rows: list[tuple[int, str, str, int]],
) -> None:
    conn.executemany(
        """
        INSERT INTO eval_runs (workspace_id, status, created_at, latency_ms)
        VALUES (?, ?, ?, ?)
        """,
        rows,
    )


def add_workspace_status_created_index(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE INDEX idx_eval_runs_workspace_status_created
        ON eval_runs (workspace_id, status, created_at DESC)
        """
    )


def plan_for_recent_completed_runs(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 3,
) -> list[str]:
    rows = conn.execute(
        """
        EXPLAIN QUERY PLAN
        SELECT id, created_at
        FROM eval_runs
        WHERE workspace_id = ?
          AND status = 'completed'
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (workspace_id, limit),
    ).fetchall()
    return [detail for _, _, _, detail in rows]


def recent_completed_runs(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 3,
) -> list[tuple[int, str]]:
    rows = conn.execute(
        """
        SELECT id, created_at
        FROM eval_runs
        WHERE workspace_id = ?
          AND status = 'completed'
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (workspace_id, limit),
    ).fetchall()
    return [(run_id, created_at) for run_id, created_at in rows]

"""partial_indexes - narrow indexes for hot subsets of a table."""

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
            created_at TEXT NOT NULL
        )
        """
    )


def seed_eval_runs(conn: sqlite3.Connection, rows: list[tuple[int, str, str]]) -> None:
    conn.executemany(
        """
        INSERT INTO eval_runs (workspace_id, status, created_at)
        VALUES (?, ?, ?)
        """,
        rows,
    )


def add_failed_runs_partial_index(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE INDEX idx_eval_runs_failed_recent
        ON eval_runs (workspace_id, created_at DESC)
        WHERE status = 'failed'
        """
    )


def plan_for_recent_failed_runs(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 2,
) -> list[str]:
    rows = conn.execute(
        """
        EXPLAIN QUERY PLAN
        SELECT id, created_at
        FROM eval_runs
        WHERE workspace_id = ?
          AND status = 'failed'
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (workspace_id, limit),
    ).fetchall()
    return [detail for _, _, _, detail in rows]


def plan_for_recent_completed_runs(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 2,
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


def plan_flags(plan_details: list[str]) -> dict[str, bool]:
    joined = " | ".join(plan_details)
    return {
        "full_scan": "SCAN eval_runs" in joined,
        "uses_partial_index": "idx_eval_runs_failed_recent" in joined,
        "temp_sort": "USE TEMP B-TREE FOR ORDER BY" in joined,
    }

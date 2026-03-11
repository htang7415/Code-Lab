"""composite_index_order - why left-prefix index order matters."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_runs_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE runs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )


def seed_runs(
    conn: sqlite3.Connection,
    rows: list[tuple[int, str, str]],
) -> None:
    conn.executemany(
        """
        INSERT INTO runs (workspace_id, status, created_at)
        VALUES (?, ?, ?)
        """,
        rows,
    )


def add_bad_index_status_workspace_created(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE INDEX idx_runs_status_workspace_created
        ON runs (status, workspace_id, created_at DESC)
        """
    )


def add_good_index_workspace_created(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE INDEX idx_runs_workspace_created
        ON runs (workspace_id, created_at DESC)
        """
    )


def plan_for_workspace_recent_runs(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 2,
) -> list[str]:
    rows = conn.execute(
        """
        EXPLAIN QUERY PLAN
        SELECT id, created_at
        FROM runs
        WHERE workspace_id = ?
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (workspace_id, limit),
    ).fetchall()
    return [detail for _, _, _, detail in rows]


def plan_flags(plan_details: list[str]) -> dict[str, bool]:
    joined = " | ".join(plan_details)
    return {
        "full_scan": "SCAN runs" in joined,
        "uses_bad_index": "idx_runs_status_workspace_created" in joined,
        "uses_good_index": "idx_runs_workspace_created" in joined,
        "temp_sort": "USE TEMP B-TREE FOR ORDER BY" in joined,
    }


def recent_runs_for_workspace(
    conn: sqlite3.Connection,
    workspace_id: int,
    limit: int = 2,
) -> list[tuple[int, str]]:
    rows = conn.execute(
        """
        SELECT id, created_at
        FROM runs
        WHERE workspace_id = ?
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (workspace_id, limit),
    ).fetchall()
    return [(run_id, created_at) for run_id, created_at in rows]

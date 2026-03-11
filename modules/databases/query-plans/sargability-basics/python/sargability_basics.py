"""sargability_basics - compare index-searchable predicates to scan-only ones."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_event_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_day TEXT NOT NULL,
            payload TEXT NOT NULL
        )
        """
    )


def seed_events(conn: sqlite3.Connection, days: list[str]) -> None:
    conn.executemany(
        """
        INSERT INTO events (created_day, payload)
        VALUES (?, ?)
        """,
        [(day, f"payload-{index}") for index, day in enumerate(days, start=1)],
    )


def add_created_day_index(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE INDEX idx_events_created_day
        ON events (created_day)
        """
    )


def plan_details(
    conn: sqlite3.Connection,
    sql: str,
    params: tuple[object, ...],
) -> list[str]:
    rows = conn.execute(f"EXPLAIN QUERY PLAN {sql}", params).fetchall()
    return [detail for _, _, _, detail in rows]


def sargable_range_plan(
    conn: sqlite3.Connection,
    start_day: str,
    end_day: str,
) -> list[str]:
    return plan_details(
        conn,
        """
        SELECT id
        FROM events
        WHERE created_day >= ? AND created_day < ?
        """,
        (start_day, end_day),
    )


def nonsargable_month_plan(
    conn: sqlite3.Connection,
    month_prefix: str,
) -> list[str]:
    return plan_details(
        conn,
        """
        SELECT id
        FROM events
        WHERE substr(created_day, 1, 7) = ?
        """,
        (month_prefix,),
    )


def plan_summary(details: list[str]) -> dict[str, bool]:
    joined = " | ".join(details)
    return {
        "uses_index_search": "SEARCH" in joined and "USING" in joined,
        "uses_scan": "SCAN" in joined,
    }


def count_rows_in_range(
    conn: sqlite3.Connection,
    start_day: str,
    end_day: str,
) -> int:
    row = conn.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE created_day >= ? AND created_day < ?
        """,
        (start_day, end_day),
    ).fetchone()
    assert row is not None
    return int(row[0])


def count_rows_for_month(conn: sqlite3.Connection, month_prefix: str) -> int:
    row = conn.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE substr(created_day, 1, 7) = ?
        """,
        (month_prefix,),
    ).fetchone()
    assert row is not None
    return int(row[0])

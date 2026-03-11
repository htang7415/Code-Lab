"""cohort_retention_basics - cohort sizes and retained users by month age."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_retention_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE users (
            user_id TEXT PRIMARY KEY,
            cohort_month TEXT NOT NULL
        );

        CREATE TABLE monthly_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            activity_month TEXT NOT NULL,
            UNIQUE (user_id, activity_month)
        );
        """
    )


def insert_user(conn: sqlite3.Connection, user_id: str, cohort_month: str) -> None:
    conn.execute(
        """
        INSERT INTO users (user_id, cohort_month)
        VALUES (?, ?)
        """,
        (user_id, cohort_month),
    )


def insert_activity(conn: sqlite3.Connection, user_id: str, activity_month: str) -> None:
    conn.execute(
        """
        INSERT INTO monthly_activity (user_id, activity_month)
        VALUES (?, ?)
        """,
        (user_id, activity_month),
    )


def cohort_sizes(conn: sqlite3.Connection) -> list[tuple[str, int]]:
    rows = conn.execute(
        """
        SELECT cohort_month, COUNT(*) AS cohort_size
        FROM users
        GROUP BY cohort_month
        ORDER BY cohort_month
        """
    ).fetchall()
    return [(cohort_month, int(cohort_size)) for cohort_month, cohort_size in rows]


def retained_users_by_period(conn: sqlite3.Connection) -> list[tuple[str, int, int]]:
    rows = conn.execute(
        """
        WITH activity_periods AS (
            SELECT
                u.cohort_month,
                (
                    (CAST(substr(a.activity_month, 1, 4) AS INTEGER) * 12 + CAST(substr(a.activity_month, 6, 2) AS INTEGER))
                    - (CAST(substr(u.cohort_month, 1, 4) AS INTEGER) * 12 + CAST(substr(u.cohort_month, 6, 2) AS INTEGER))
                ) AS period_number,
                a.user_id
            FROM monthly_activity AS a
            JOIN users AS u ON u.user_id = a.user_id
            WHERE a.activity_month >= u.cohort_month
        )
        SELECT cohort_month, period_number, COUNT(DISTINCT user_id) AS retained_users
        FROM activity_periods
        GROUP BY cohort_month, period_number
        ORDER BY cohort_month, period_number
        """
    ).fetchall()
    return [
        (cohort_month, int(period_number), int(retained_users))
        for cohort_month, period_number, retained_users in rows
    ]


def retention_rates(conn: sqlite3.Connection) -> list[tuple[str, int, float]]:
    sizes = dict(cohort_sizes(conn))
    rates: list[tuple[str, int, float]] = []
    for cohort_month, period_number, retained_users in retained_users_by_period(conn):
        cohort_size = sizes[cohort_month]
        rates.append((cohort_month, period_number, retained_users / cohort_size))
    return rates

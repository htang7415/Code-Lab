"""upserts_and_merge_patterns - insert-or-update writes with freshness checks."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_model_scores_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE model_scores (
            model_name TEXT NOT NULL,
            dataset_name TEXT NOT NULL,
            score REAL NOT NULL,
            updated_at TEXT NOT NULL,
            PRIMARY KEY (model_name, dataset_name)
        )
        """
    )


def upsert_score(
    conn: sqlite3.Connection,
    model_name: str,
    dataset_name: str,
    score: float,
    updated_at: str,
) -> None:
    conn.execute(
        """
        INSERT INTO model_scores (model_name, dataset_name, score, updated_at)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(model_name, dataset_name) DO UPDATE SET
            score = excluded.score,
            updated_at = excluded.updated_at
        WHERE excluded.updated_at >= model_scores.updated_at
        """,
        (model_name, dataset_name, score, updated_at),
    )


def merge_score_batch(
    conn: sqlite3.Connection,
    rows: list[tuple[str, str, float, str]],
) -> None:
    for row in rows:
        upsert_score(conn, *row)


def score_rows(conn: sqlite3.Connection) -> list[tuple[str, str, float, str]]:
    rows = conn.execute(
        """
        SELECT model_name, dataset_name, score, updated_at
        FROM model_scores
        ORDER BY model_name, dataset_name
        """
    ).fetchall()
    return [(model_name, dataset_name, score, updated_at) for model_name, dataset_name, score, updated_at in rows]

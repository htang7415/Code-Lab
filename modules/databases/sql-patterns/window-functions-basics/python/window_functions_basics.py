"""window_functions_basics - ranking and deltas with SQL window functions."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_eval_results_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE eval_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT NOT NULL,
            dataset_name TEXT NOT NULL,
            score REAL NOT NULL,
            recorded_at TEXT NOT NULL
        )
        """
    )


def record_eval_result(
    conn: sqlite3.Connection,
    model_name: str,
    dataset_name: str,
    score: float,
    recorded_at: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO eval_results (model_name, dataset_name, score, recorded_at)
        VALUES (?, ?, ?, ?)
        """,
        (model_name, dataset_name, score, recorded_at),
    )
    return int(cursor.lastrowid)


def rank_runs_within_model(conn: sqlite3.Connection) -> list[dict[str, object]]:
    rows = conn.execute(
        """
        SELECT
            model_name,
            dataset_name,
            score,
            recorded_at,
            ROW_NUMBER() OVER (
                PARTITION BY model_name
                ORDER BY score DESC, recorded_at DESC, id DESC
            ) AS rank_in_model
        FROM eval_results
        ORDER BY model_name, rank_in_model
        """
    ).fetchall()
    return [
        {
            "model_name": model_name,
            "dataset_name": dataset_name,
            "score": score,
            "recorded_at": recorded_at,
            "rank_in_model": rank_in_model,
        }
        for model_name, dataset_name, score, recorded_at, rank_in_model in rows
    ]


def best_run_per_model(conn: sqlite3.Connection) -> list[dict[str, object]]:
    rows = conn.execute(
        """
        WITH ranked AS (
            SELECT
                id,
                model_name,
                dataset_name,
                score,
                recorded_at,
                ROW_NUMBER() OVER (
                    PARTITION BY model_name
                    ORDER BY score DESC, recorded_at DESC, id DESC
                ) AS rank_in_model
            FROM eval_results
        )
        SELECT model_name, dataset_name, score, recorded_at
        FROM ranked
        WHERE rank_in_model = 1
        ORDER BY model_name
        """
    ).fetchall()
    return [
        {
            "model_name": model_name,
            "dataset_name": dataset_name,
            "score": score,
            "recorded_at": recorded_at,
        }
        for model_name, dataset_name, score, recorded_at in rows
    ]


def score_deltas_by_model(conn: sqlite3.Connection) -> list[dict[str, object]]:
    rows = conn.execute(
        """
        SELECT
            model_name,
            dataset_name,
            score,
            recorded_at,
            score - LAG(score) OVER (
                PARTITION BY model_name
                ORDER BY recorded_at, id
            ) AS delta_from_previous
        FROM eval_results
        ORDER BY model_name, recorded_at, id
        """
    ).fetchall()
    return [
        {
            "model_name": model_name,
            "dataset_name": dataset_name,
            "score": score,
            "recorded_at": recorded_at,
            "delta_from_previous": delta,
        }
        for model_name, dataset_name, score, recorded_at, delta in rows
    ]

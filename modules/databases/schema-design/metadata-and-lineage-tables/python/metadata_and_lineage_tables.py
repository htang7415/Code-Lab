"""metadata_and_lineage_tables - explicit metadata and lineage edge tables."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_metadata_lineage_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE assets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            kind TEXT NOT NULL,
            uri TEXT NOT NULL,
            content_hash TEXT NOT NULL,
            UNIQUE (workspace_id, uri)
        );

        CREATE TABLE jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            job_kind TEXT NOT NULL,
            model_name TEXT NOT NULL,
            created_at TEXT NOT NULL
        );

        CREATE TABLE job_inputs (
            job_id INTEGER NOT NULL,
            asset_id INTEGER NOT NULL,
            input_role TEXT NOT NULL,
            PRIMARY KEY (job_id, asset_id, input_role),
            FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE,
            FOREIGN KEY (asset_id) REFERENCES assets(id) ON DELETE CASCADE
        );

        CREATE TABLE job_outputs (
            job_id INTEGER NOT NULL,
            asset_id INTEGER NOT NULL UNIQUE,
            output_role TEXT NOT NULL,
            PRIMARY KEY (job_id, asset_id, output_role),
            FOREIGN KEY (job_id) REFERENCES jobs(id) ON DELETE CASCADE,
            FOREIGN KEY (asset_id) REFERENCES assets(id) ON DELETE CASCADE
        );
        """
    )


def insert_asset(
    conn: sqlite3.Connection,
    workspace_id: int,
    kind: str,
    uri: str,
    content_hash: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO assets (workspace_id, kind, uri, content_hash)
        VALUES (?, ?, ?, ?)
        """,
        (workspace_id, kind, uri, content_hash),
    )
    return int(cursor.lastrowid)


def insert_job(
    conn: sqlite3.Connection,
    workspace_id: int,
    job_kind: str,
    model_name: str,
    created_at: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO jobs (workspace_id, job_kind, model_name, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (workspace_id, job_kind, model_name, created_at),
    )
    return int(cursor.lastrowid)


def link_job_input(
    conn: sqlite3.Connection,
    job_id: int,
    asset_id: int,
    input_role: str,
) -> None:
    conn.execute(
        """
        INSERT INTO job_inputs (job_id, asset_id, input_role)
        VALUES (?, ?, ?)
        """,
        (job_id, asset_id, input_role),
    )


def link_job_output(
    conn: sqlite3.Connection,
    job_id: int,
    asset_id: int,
    output_role: str = "primary",
) -> None:
    conn.execute(
        """
        INSERT INTO job_outputs (job_id, asset_id, output_role)
        VALUES (?, ?, ?)
        """,
        (job_id, asset_id, output_role),
    )


def lineage_summary(conn: sqlite3.Connection, job_id: int) -> dict[str, object]:
    job_row = conn.execute(
        """
        SELECT job_kind, model_name, created_at
        FROM jobs
        WHERE id = ?
        """,
        (job_id,),
    ).fetchone()
    if job_row is None:
        raise ValueError(f"missing job {job_id}")

    input_rows = conn.execute(
        """
        SELECT ji.input_role, a.uri
        FROM job_inputs AS ji
        JOIN assets AS a ON a.id = ji.asset_id
        WHERE ji.job_id = ?
        ORDER BY ji.input_role, a.uri
        """,
        (job_id,),
    ).fetchall()
    output_rows = conn.execute(
        """
        SELECT jo.output_role, a.uri
        FROM job_outputs AS jo
        JOIN assets AS a ON a.id = jo.asset_id
        WHERE jo.job_id = ?
        ORDER BY jo.output_role, a.uri
        """,
        (job_id,),
    ).fetchall()

    return {
        "job_kind": job_row[0],
        "model_name": job_row[1],
        "created_at": job_row[2],
        "inputs": [{"role": role, "uri": uri} for role, uri in input_rows],
        "outputs": [{"role": role, "uri": uri} for role, uri in output_rows],
    }

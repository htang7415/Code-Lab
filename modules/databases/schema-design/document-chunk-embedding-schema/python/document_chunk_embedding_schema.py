"""document_chunk_embedding_schema - normalized retrieval schema with lineage."""

from __future__ import annotations

import json
import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_ai_retrieval_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            workspace_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            source_uri TEXT
        );

        CREATE TABLE chunks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL,
            chunk_index INTEGER NOT NULL,
            text TEXT NOT NULL,
            token_count INTEGER NOT NULL,
            FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE CASCADE,
            UNIQUE (document_id, chunk_index)
        );

        CREATE TABLE embedding_jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            model_name TEXT NOT NULL,
            dimensions INTEGER NOT NULL
        );

        CREATE TABLE chunk_embeddings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chunk_id INTEGER NOT NULL,
            embedding_job_id INTEGER NOT NULL,
            vector_json TEXT NOT NULL,
            FOREIGN KEY (chunk_id) REFERENCES chunks(id) ON DELETE CASCADE,
            FOREIGN KEY (embedding_job_id) REFERENCES embedding_jobs(id) ON DELETE CASCADE,
            UNIQUE (chunk_id, embedding_job_id)
        );
        """
    )


def insert_document(
    conn: sqlite3.Connection,
    workspace_id: int,
    title: str,
    source_uri: str | None = None,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO documents (workspace_id, title, source_uri)
        VALUES (?, ?, ?)
        """,
        (workspace_id, title, source_uri),
    )
    return int(cursor.lastrowid)


def insert_chunk(
    conn: sqlite3.Connection,
    document_id: int,
    chunk_index: int,
    text: str,
) -> int:
    token_count = len(text.split())
    cursor = conn.execute(
        """
        INSERT INTO chunks (document_id, chunk_index, text, token_count)
        VALUES (?, ?, ?, ?)
        """,
        (document_id, chunk_index, text, token_count),
    )
    return int(cursor.lastrowid)


def insert_embedding_job(
    conn: sqlite3.Connection,
    model_name: str,
    dimensions: int,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO embedding_jobs (model_name, dimensions)
        VALUES (?, ?)
        """,
        (model_name, dimensions),
    )
    return int(cursor.lastrowid)


def attach_chunk_embedding(
    conn: sqlite3.Connection,
    chunk_id: int,
    embedding_job_id: int,
    vector: list[float],
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO chunk_embeddings (chunk_id, embedding_job_id, vector_json)
        VALUES (?, ?, ?)
        """,
        (chunk_id, embedding_job_id, json.dumps(vector)),
    )
    return int(cursor.lastrowid)


def list_document_embeddings(
    conn: sqlite3.Connection,
    document_id: int,
) -> list[dict[str, object]]:
    rows = conn.execute(
        """
        SELECT
            c.chunk_index,
            c.text,
            c.token_count,
            ej.model_name,
            ej.dimensions,
            ce.vector_json
        FROM chunks AS c
        JOIN chunk_embeddings AS ce ON ce.chunk_id = c.id
        JOIN embedding_jobs AS ej ON ej.id = ce.embedding_job_id
        WHERE c.document_id = ?
        ORDER BY c.chunk_index, ej.model_name
        """,
        (document_id,),
    ).fetchall()
    return [
        {
            "chunk_index": chunk_index,
            "chunk_text": chunk_text,
            "token_count": token_count,
            "model_name": model_name,
            "dimensions": dimensions,
            "vector": json.loads(vector_json),
        }
        for chunk_index, chunk_text, token_count, model_name, dimensions, vector_json in rows
    ]

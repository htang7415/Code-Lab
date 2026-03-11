import sqlite3

import pytest

from document_chunk_embedding_schema import (
    attach_chunk_embedding,
    create_ai_retrieval_schema,
    create_connection,
    insert_chunk,
    insert_document,
    insert_embedding_job,
    list_document_embeddings,
)


def test_embedding_rows_preserve_chunk_and_job_lineage() -> None:
    conn = create_connection()
    create_ai_retrieval_schema(conn)
    document_id = insert_document(conn, 42, "agent-spec", "s3://spec.md")
    chunk_id = insert_chunk(conn, document_id, 0, "Agent memory needs retrieval scoring.")
    job_id = insert_embedding_job(conn, "text-embedding-3-small", 3)

    attach_chunk_embedding(conn, chunk_id, job_id, [0.1, 0.2, 0.3])

    assert list_document_embeddings(conn, document_id) == [
        {
            "chunk_index": 0,
            "chunk_text": "Agent memory needs retrieval scoring.",
            "token_count": 5,
            "model_name": "text-embedding-3-small",
            "dimensions": 3,
            "vector": [0.1, 0.2, 0.3],
        }
    ]


def test_same_chunk_and_job_cannot_be_embedded_twice() -> None:
    conn = create_connection()
    create_ai_retrieval_schema(conn)
    document_id = insert_document(conn, 42, "agent-spec")
    chunk_id = insert_chunk(conn, document_id, 0, "Agent memory needs retrieval scoring.")
    job_id = insert_embedding_job(conn, "text-embedding-3-small", 3)

    attach_chunk_embedding(conn, chunk_id, job_id, [0.1, 0.2, 0.3])

    with pytest.raises(sqlite3.IntegrityError):
        attach_chunk_embedding(conn, chunk_id, job_id, [0.4, 0.5, 0.6])


def test_rows_are_sorted_by_chunk_index_then_model_name() -> None:
    conn = create_connection()
    create_ai_retrieval_schema(conn)
    document_id = insert_document(conn, 42, "agent-spec")
    later_chunk_id = insert_chunk(conn, document_id, 1, "Later chunk.")
    earlier_chunk_id = insert_chunk(conn, document_id, 0, "Earlier chunk.")
    large_job_id = insert_embedding_job(conn, "text-embedding-3-large", 3)
    small_job_id = insert_embedding_job(conn, "text-embedding-3-small", 3)

    attach_chunk_embedding(conn, later_chunk_id, small_job_id, [0.9, 0.1, 0.2])
    attach_chunk_embedding(conn, earlier_chunk_id, large_job_id, [0.3, 0.4, 0.5])
    attach_chunk_embedding(conn, earlier_chunk_id, small_job_id, [0.1, 0.2, 0.3])

    rows = list_document_embeddings(conn, document_id)

    assert [row["chunk_index"] for row in rows] == [0, 0, 1]
    assert [row["model_name"] for row in rows] == [
        "text-embedding-3-large",
        "text-embedding-3-small",
        "text-embedding-3-small",
    ]

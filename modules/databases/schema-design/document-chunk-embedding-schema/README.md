# Document Chunk Embedding Schema

> Track: `databases` | Topic: `schema-design`

## Concept

A retrieval system usually needs separate tables for documents, chunks, embedding jobs, and embeddings so that content, lineage, and model metadata stay queryable.

## Key Points

- Keep document metadata separate from chunk rows.
- Record which embedding job produced each vector so you can re-embed safely later.
- Use uniqueness constraints to prevent duplicate chunk positions or duplicate embeddings for the same chunk and job.
- Schema design for AI systems is mostly normal schema design plus lineage.

## Minimal Code Mental Model

```python
conn = create_connection()
create_ai_retrieval_schema(conn)
document_id = insert_document(conn, 42, "spec")
chunk_id = insert_chunk(conn, document_id, 0, "Agent memory needs retrieval.")
job_id = insert_embedding_job(conn, "text-embedding-3-small", 3)
attach_chunk_embedding(conn, chunk_id, job_id, [0.1, 0.2, 0.3])
rows = list_document_embeddings(conn, document_id)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_ai_retrieval_schema(conn: sqlite3.Connection) -> None:
def insert_document(
    conn: sqlite3.Connection,
    workspace_id: int,
    title: str,
    source_uri: str | None = None,
) -> int:
def insert_chunk(
    conn: sqlite3.Connection,
    document_id: int,
    chunk_index: int,
    text: str,
) -> int:
def insert_embedding_job(conn: sqlite3.Connection, model_name: str, dimensions: int) -> int:
def attach_chunk_embedding(
    conn: sqlite3.Connection,
    chunk_id: int,
    embedding_job_id: int,
    vector: list[float],
) -> int:
def list_document_embeddings(
    conn: sqlite3.Connection,
    document_id: int,
) -> list[dict[str, object]]:
```

## Run tests

```bash
pytest modules/databases/schema-design/document-chunk-embedding-schema/python -q
```

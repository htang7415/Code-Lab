# Tables And Keys

> Track: `databases` | Topic: `relational`

## Concept

Tables hold entities, primary keys identify rows, and foreign keys connect related rows without relying on application-only conventions.

## Key Points

- Primary keys give each row a stable identity.
- Foreign keys protect relationships like `chunks -> documents`.
- Composite uniqueness rules often encode product rules directly in the schema.
- A left join lets you ask for all parent rows even when some children do not exist yet.

## Minimal Code Mental Model

```python
conn = create_connection()
create_core_tables(conn)
workspace_id = insert_workspace(conn, "research")
document_id = insert_document(conn, workspace_id, "rag-notes")
insert_chunk(conn, document_id, 0, "Chunk zero")
counts = chunk_counts_by_document(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_core_tables(conn: sqlite3.Connection) -> None:
def insert_workspace(conn: sqlite3.Connection, name: str) -> int:
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
def chunk_counts_by_document(conn: sqlite3.Connection) -> list[tuple[str, str, int]]:
```

## Run tests

```bash
pytest modules/databases/relational/tables-and-keys/python -q
```

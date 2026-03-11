# Optimistic Concurrency Control

> Track: `databases` | Topic: `transactions`

## Concept

Optimistic concurrency control lets multiple readers work without locks first, then rejects a write if the row changed underneath them. The usual shape is a version column with a compare-and-swap update.

## Key Points

- Readers carry the version they saw.
- Writers update with `WHERE id = ? AND version = ?`.
- If zero rows changed, the write lost the race and must retry or re-read.
- This pattern works well when collisions are possible but not constant.

## Minimal Code Mental Model

```python
doc = read_document(conn, document_id)
ok = update_document_if_version(conn, document_id, doc["version"], "published")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_document_table(conn: sqlite3.Connection) -> None:
def insert_document(conn: sqlite3.Connection, title: str, status: str) -> int:
def read_document(conn: sqlite3.Connection, document_id: int) -> dict[str, object]:
def update_document_if_version(
    conn: sqlite3.Connection,
    document_id: int,
    expected_version: int,
    new_status: str,
) -> bool:
```

## Run tests

```bash
pytest modules/databases/transactions/optimistic-concurrency-control/python -q
```

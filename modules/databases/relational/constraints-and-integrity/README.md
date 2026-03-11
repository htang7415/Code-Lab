# Constraints And Integrity

> Track: `databases` | Topic: `relational`

## Concept

Constraints keep bad states out of the database before they turn into application bugs.

## Key Points

- `NOT NULL` protects required fields.
- `UNIQUE` enforces business rules like one document title per workspace.
- `CHECK` constrains valid values such as allowed statuses.
- Foreign keys keep child rows attached to real parent rows.

## Minimal Code Mental Model

```python
conn = create_connection()
create_integrity_schema(conn)
workspace_id = insert_workspace(conn, "research")
insert_document(conn, workspace_id, "spec", "draft")
rows = document_rows(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_integrity_schema(conn: sqlite3.Connection) -> None:
def insert_workspace(conn: sqlite3.Connection, name: str) -> int:
def insert_document(
    conn: sqlite3.Connection,
    workspace_id: int,
    title: str,
    status: str,
) -> int:
def document_rows(conn: sqlite3.Connection) -> list[tuple[str, str, str]]:
```

## Run tests

```bash
pytest modules/databases/relational/constraints-and-integrity/python -q
```

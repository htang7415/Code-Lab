# JSONB To Normalized Migration

> Track: `databases` | Topic: `relational`

## Concept

When a JSON-like field becomes a hot query path, migrate the frequently-filtered attributes into normal relational tables instead of repeatedly parsing the blob.

## Key Points

- JSON metadata is fine for low-frequency or evolving attributes.
- Once a field becomes a join or filter key, backfilling a normalized table is usually cleaner than adding more blob parsing.
- A migration can keep the original JSON for compatibility while introducing indexed relational rows.
- Good backfills are idempotent so they can be rerun safely.

## Minimal Code Mental Model

```python
conn = create_connection()
create_legacy_schema(conn)
ticket_id = insert_legacy_ticket(conn, 7, "Broken retrieval", {"tags": ["rag", "prod"]})
create_normalized_tag_table(conn)
backfill_ticket_tags(conn)
matches = tickets_with_tag_from_normalized(conn, workspace_id=7, tag="rag")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_legacy_schema(conn: sqlite3.Connection) -> None:
def insert_legacy_ticket(
    conn: sqlite3.Connection,
    workspace_id: int,
    title: str,
    metadata: dict[str, object],
) -> int:
def create_normalized_tag_table(conn: sqlite3.Connection) -> None:
def backfill_ticket_tags(conn: sqlite3.Connection) -> None:
def tickets_with_tag_from_json(
    conn: sqlite3.Connection,
    workspace_id: int,
    tag: str,
) -> list[int]:
def tickets_with_tag_from_normalized(
    conn: sqlite3.Connection,
    workspace_id: int,
    tag: str,
) -> list[int]:
def tag_rows(conn: sqlite3.Connection) -> list[tuple[int, str]]:
```

## Run tests

```bash
pytest modules/databases/relational/jsonb-to-normalized-migration/python -q
```

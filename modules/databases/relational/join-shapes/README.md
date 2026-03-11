# Join Shapes

> Track: `databases` | Topic: `relational`

## Concept

Different join shapes answer different questions: an inner join keeps only matching rows, a left join keeps all rows from the left table, and an anti-join finds rows with no match.

## Key Points

- Inner joins answer "show me matching parent-child pairs."
- Left joins answer "show me every parent, even if it has zero children."
- Anti-joins answer "which parents are missing children?"
- Picking the wrong join shape is a correctness bug, not just a style issue.

## Minimal Code Mental Model

```python
conn = create_connection()
create_join_demo_tables(conn)
seed_documents(conn, [(1, "spec"), (2, "roadmap"), (3, "notes")])
seed_chunks(conn, [(1, 0, "chunk a"), (1, 1, "chunk b"), (3, 0, "chunk c")])
pairs = inner_join_document_chunks(conn)
counts = left_join_document_chunk_counts(conn)
missing = documents_without_chunks(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_join_demo_tables(conn: sqlite3.Connection) -> None:
def seed_documents(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
def seed_chunks(
    conn: sqlite3.Connection,
    rows: list[tuple[int, int, str]],
) -> None:
def inner_join_document_chunks(conn: sqlite3.Connection) -> list[tuple[str, str]]:
def left_join_document_chunk_counts(conn: sqlite3.Connection) -> list[tuple[str, int]]:
def documents_without_chunks(conn: sqlite3.Connection) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/relational/join-shapes/python -q
```

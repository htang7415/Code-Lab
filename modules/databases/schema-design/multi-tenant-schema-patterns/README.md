# Multi Tenant Schema Patterns

> Track: `databases` | Topic: `schema-design`

## Concept

Multi-tenant schemas keep each customer's data isolated while still sharing one database and one set of tables.

## Key Points

- Tenant identity should be explicit in every tenant-scoped table.
- Composite constraints can stop cross-tenant references before they reach application code.
- Uniqueness rules often belong inside a tenant, not globally across all tenants.
- A good multi-tenant schema makes isolation the default query shape.

## Minimal Code Mental Model

```python
conn = create_connection()
create_multi_tenant_schema(conn)
team_a = insert_workspace(conn, "team-a")
team_b = insert_workspace(conn, "team-b")
doc_id = insert_document(conn, team_a, "spec")
insert_chunk(conn, team_a, doc_id, 0, "chunk a")
docs = document_titles_for_workspace(conn, team_a)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_multi_tenant_schema(conn: sqlite3.Connection) -> None:
def insert_workspace(conn: sqlite3.Connection, name: str) -> int:
def insert_document(conn: sqlite3.Connection, workspace_id: int, title: str) -> int:
def insert_chunk(
    conn: sqlite3.Connection,
    workspace_id: int,
    document_id: int,
    chunk_index: int,
    text: str,
) -> int:
def document_titles_for_workspace(
    conn: sqlite3.Connection,
    workspace_id: int,
) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/schema-design/multi-tenant-schema-patterns/python -q
```

# Metadata And Lineage Tables

> Track: `databases` | Topic: `schema-design`

## Concept

Metadata tables describe assets and jobs, while lineage tables record which jobs consumed or produced which assets.

## Key Points

- Asset metadata should be queryable without scanning raw payloads.
- Input and output edges should be explicit tables, not buried in blobs.
- A produced asset should normally have one producer job in the lineage graph.
- Lineage lets you answer “which prompt, dataset, and model produced this output?”

## Minimal Code Mental Model

```python
conn = create_connection()
create_metadata_lineage_schema(conn)
dataset_id = insert_asset(conn, 42, "dataset", "s3://datasets/v1.parquet", "abc")
job_id = insert_job(conn, 42, "eval", "gpt-4.1-mini", "2026-03-11T10:00:00Z")
link_job_input(conn, job_id, dataset_id, "dataset")
summary = lineage_summary(conn, job_id)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_metadata_lineage_schema(conn: sqlite3.Connection) -> None:
def insert_asset(
    conn: sqlite3.Connection,
    workspace_id: int,
    kind: str,
    uri: str,
    content_hash: str,
) -> int:
def insert_job(
    conn: sqlite3.Connection,
    workspace_id: int,
    job_kind: str,
    model_name: str,
    created_at: str,
) -> int:
def link_job_input(
    conn: sqlite3.Connection,
    job_id: int,
    asset_id: int,
    input_role: str,
) -> None:
def link_job_output(
    conn: sqlite3.Connection,
    job_id: int,
    asset_id: int,
    output_role: str = "primary",
) -> None:
def lineage_summary(conn: sqlite3.Connection, job_id: int) -> dict[str, object]:
```

## Run tests

```bash
pytest modules/databases/schema-design/metadata-and-lineage-tables/python -q
```

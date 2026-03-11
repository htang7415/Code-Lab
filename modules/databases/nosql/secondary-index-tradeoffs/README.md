# Secondary Index Tradeoffs

> Track: `databases` | Topic: `nosql`

## Concept

Secondary indexes speed up alternate lookup paths, but they add extra write work because the index has to stay in sync with the primary document store.

## Key Points

- A primary key lookup is cheap because the store is already organized around it.
- A secondary index lets you query by another field like `status`.
- Updating an indexed field usually means removing one old index entry and adding one new one.
- Secondary indexes improve reads but increase write amplification and maintenance complexity.

## Minimal Code Mental Model

```python
store = {}
status_index = {}
put_document(store, status_index, "job-1", {"status": "queued", "owner": "ops"})
put_document(store, status_index, "job-1", {"status": "running", "owner": "ops"})
queued = documents_by_status(store, status_index, "queued")
```

## Function

```python
def put_document(
    store: dict[str, dict[str, object]],
    status_index: dict[str, set[str]],
    doc_id: str,
    document: dict[str, object],
) -> int:
def documents_by_status(
    store: dict[str, dict[str, object]],
    status_index: dict[str, set[str]],
    status: str,
) -> list[dict[str, object]]:
def index_updates_for_write(previous_status: str | None, new_status: str) -> int:
```

## Run tests

```bash
pytest modules/databases/nosql/secondary-index-tradeoffs/python -q
```

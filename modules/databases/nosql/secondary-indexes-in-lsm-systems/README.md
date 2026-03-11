# Secondary Indexes In LSM Systems

> Track: `databases` | Topic: `nosql`

## Concept

Secondary indexes in LSM-style systems make new query patterns possible, but every extra index usually adds another write path and more compaction work.

## Key Points

- A primary-key write is usually one write path.
- Each secondary index often adds another write entry for the same logical row.
- Secondary indexes help lookup by non-key fields, but they are not free.
- Non-unique index values can point to many row IDs, so read fanout still matters.

## Minimal Code Mental Model

```python
rows = [
    {"id": "u1", "email": "a@example.com", "tier": "pro"},
    {"id": "u2", "email": "b@example.com", "tier": "pro"},
]
index = build_secondary_index(rows, "tier")
ids = lookup_secondary(index, "pro")
cost = write_entries_per_row(index_count=2)
```

## Function

```python
def write_entries_per_row(index_count: int) -> int:
def build_secondary_index(
    rows: list[dict[str, object]],
    field: str,
) -> dict[object, list[str]]:
def lookup_secondary(
    index: dict[object, list[str]],
    value: object,
) -> list[str]:
def storage_entries(row_count: int, index_count: int) -> int:
```

## Run tests

```bash
pytest modules/databases/nosql/secondary-indexes-in-lsm-systems/python -q
```

# MVCC Mental Model

> Track: `databases` | Topic: `transactions`

## Concept

MVCC keeps old row versions so each transaction can read a stable snapshot without blocking every writer.

## Key Points

- Visibility depends on transaction snapshot time, not just the latest committed row.
- Updates usually create a new version and mark the old version as deleted later.
- An older snapshot can keep seeing the old value while a newer snapshot sees the new one.
- Thinking in versions is the clearest way to understand snapshot isolation.

## Minimal Code Mental Model

```python
store = {}
append_version(store, "doc-1", "draft", created_xid=10)
replace_visible_value(store, "doc-1", "published", writer_xid=11)
old_view = visible_value(store, "doc-1", snapshot_xid=10)
new_view = visible_value(store, "doc-1", snapshot_xid=11)
```

## Function

```python
@dataclass
class RowVersion:
    value: object
    created_xid: int
    deleted_xid: int | None = None

def append_version(
    store: dict[str, list[RowVersion]],
    key: str,
    value: object,
    created_xid: int,
) -> None:
def replace_visible_value(
    store: dict[str, list[RowVersion]],
    key: str,
    new_value: object,
    writer_xid: int,
) -> None:
def delete_visible_value(
    store: dict[str, list[RowVersion]],
    key: str,
    writer_xid: int,
) -> None:
def visible_value(
    store: dict[str, list[RowVersion]],
    key: str,
    snapshot_xid: int,
) -> object | None:
```

## Run tests

```bash
pytest modules/databases/transactions/mvcc-mental-model/python -q
```

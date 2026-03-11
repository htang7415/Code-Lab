# Point Lookups Vs Range Scans

> Track: `databases` | Topic: `indexing`

## Concept

Point lookups pay mostly fixed index descent cost. Range scans pay that same descent cost plus extra work for every matching row the engine must keep walking.

## Key Points

- A point predicate like `id = 42` is usually bounded by tree height, not table size.
- A range predicate like `created_at >= ...` still uses the index, but read cost grows with the number of matching rows.
- Good indexes help both patterns, but they do not make large ranges free.
- Estimating result size is the difference between a cheap probe and an expensive scan.

## Minimal Code Mental Model

```python
summary = access_summary(index_height=4, matching_rows=200)
path = choose_access_path("range", matching_rows=200)
```

## Function

```python
def point_lookup_work(index_height: int) -> int:
def range_scan_work(index_height: int, matching_rows: int) -> int:
def choose_access_path(predicate_shape: str, matching_rows: int) -> str:
def access_summary(index_height: int, matching_rows: int) -> dict[str, int | str]:
```

## Run tests

```bash
pytest modules/databases/indexing/point-lookups-vs-range-scans/python -q
```

# Merge Vs Materialize OLAP Patterns

> Track: `databases` | Topic: `sql-patterns`

## Concept

Analytics systems often choose between merge-on-read and materialized summaries. Merge-on-read keeps raw deltas flexible, while materialization pays refresh work up front to make repeated reads cheap.

## Key Points

- Merge-on-read recomputes from base plus delta during query time.
- Materialized summaries shift work from query time to refresh time.
- If many dashboards reuse the same aggregate, materialization usually wins.
- If refreshes are rare and queries are few, merge-on-read can stay simpler.

## Minimal Code Mental Model

```python
merge = merge_total_work(base_rows=1_000_000, delta_rows=50_000, query_count=20)
materialized = materialize_total_work(delta_rows=50_000, query_count=20)
choice = choose_olap_pattern(base_rows=1_000_000, delta_rows=50_000, query_count=20)
```

## Function

```python
def merge_query_work(base_rows: int, delta_rows: int) -> int:
def merge_total_work(base_rows: int, delta_rows: int, query_count: int) -> int:
def materialize_refresh_work(delta_rows: int) -> int:
def materialize_total_work(delta_rows: int, query_count: int) -> int:
def choose_olap_pattern(base_rows: int, delta_rows: int, query_count: int) -> str:
def work_summary(base_rows: int, delta_rows: int, query_count: int) -> dict[str, int | str]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/merge-vs-materialize-olap-patterns/python -q
```

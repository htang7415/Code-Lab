# Cardinality Estimation

> Track: `databases` | Topic: `query-plans`

## Concept

Cardinality estimation is the optimizer’s guess about how many rows each step of a query will produce.

## Key Points

- Many plan mistakes start with a bad row-count estimate.
- A common first estimate multiplies selectivities across predicates.
- Estimated row count affects whether the optimizer prefers a scan or an index lookup.
- Q-error is a simple way to measure how wrong an estimate was.

## Math

$$
\text{estimated rows} = \text{table rows} \times \prod_i \text{selectivity}_i
$$

## Minimal Code Mental Model

```python
estimated = estimate_rows(10000, [0.1, 0.2])
scan = choose_access_path(estimated, table_rows=10000, index_available=True)
error = q_error(estimated, actual_rows=900)
```

## Function

```python
def estimate_rows(table_rows: int, selectivities: list[float]) -> int:
def choose_access_path(
    estimated_rows: int,
    table_rows: int,
    index_available: bool,
    index_fraction_threshold: float = 0.1,
) -> str:
def q_error(estimated_rows: int, actual_rows: int) -> float:
def needs_plan_attention(
    estimated_rows: int,
    actual_rows: int,
    q_error_threshold: float = 4.0,
) -> bool:
```

## Run tests

```bash
pytest modules/databases/query-plans/cardinality-estimation/python -q
```

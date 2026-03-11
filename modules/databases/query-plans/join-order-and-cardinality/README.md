# Join Order And Cardinality

> Track: `databases` | Topic: `query-plans`

## Concept

Join order follows cardinality. The optimizer wants to keep intermediate results small, so the most selective starting point is often the cheapest plan.

## Key Points

- Cardinality is the estimated number of rows after each filter or join.
- A selective filter early in the plan can shrink every downstream join.
- Starting from a huge fact table can keep intermediate results huge even when the final answer is small.
- Join order bugs are often estimation bugs before they are join-algorithm bugs.

## Minimal Code Mental Model

```python
table_rows = {"customers": 100_000, "orders": 500_000, "items": 2_000_000}
selectivities = {"customers": 0.001, "orders": 1.0, "items": 1.0}
edges = {
    ("customers", "orders"): 5.0,
    ("orders", "items"): 4.0,
}
plan = left_deep_plan_cost(table_rows, selectivities, ["customers", "orders", "items"], edges)
```

## Function

```python
def filtered_rows(base_rows: int, selectivity: float) -> int:
def join_output_rows(current_rows: int, average_matches: float) -> int:
def left_deep_plan_cost(
    table_rows: dict[str, int],
    selectivities: dict[str, float],
    join_order: list[str],
    join_edges: dict[tuple[str, str], float],
) -> dict[str, int]:
def cheaper_plan(left: dict[str, int], right: dict[str, int]) -> str:
```

## Run tests

```bash
pytest modules/databases/query-plans/join-order-and-cardinality/python -q
```

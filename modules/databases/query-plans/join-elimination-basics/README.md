# Join Elimination Basics

> Track: `databases` | Topic: `query-plans`

## Concept

Join elimination removes a redundant join when the query does not need columns or filters from that table and referential integrity already guarantees the relationship.

## Key Points

- If the parent table contributes no columns and no filter, the join may be unnecessary.
- The optimizer needs confidence that every child row already has a valid parent.
- Eliminating the join reduces lookup work without changing results.
- If you select parent columns or filter on the parent, the join still matters.

## Minimal Code Mental Model

```python
summary = plan_summary(
    child_rows=1_000,
    parent_lookup_cost=2,
    selects_parent_columns=False,
    filters_parent_rows=False,
    child_fk_not_null=True,
)
```

## Function

```python
def join_can_be_eliminated(
    selects_parent_columns: bool,
    filters_parent_rows: bool,
    child_fk_not_null: bool,
) -> bool:
def query_work(
    child_rows: int,
    parent_lookup_cost: int,
    eliminated: bool,
) -> int:
def plan_summary(
    child_rows: int,
    parent_lookup_cost: int,
    selects_parent_columns: bool,
    filters_parent_rows: bool,
    child_fk_not_null: bool,
) -> dict[str, int | bool]:
```

## Run tests

```bash
pytest modules/databases/query-plans/join-elimination-basics/python -q
```

# Join Vs Subquery Shapes

> Track: `databases` | Topic: `relational`

## Concept

Joins and subqueries can answer the same business question with different row shapes. A join can duplicate parent rows, while an `EXISTS` subquery can keep one row per parent.

## Key Points

- A join returns one row per matching pair.
- An `EXISTS` subquery returns one row per left-side row that has a match.
- If the question is “which customers have a paid order?”, `EXISTS` often matches the mental model better.
- Picking the wrong shape can create accidental duplicates or unnecessary `DISTINCT`.

## Minimal Code Mental Model

```python
conn = create_connection()
create_demo_tables(conn)
seed_customers(conn, [(1, "Ada"), (2, "Linus")])
seed_orders(conn, [(1, "paid"), (1, "paid"), (2, "draft")])
joined = join_customers_with_paid_orders(conn)
exists = subquery_customers_with_paid_orders(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_demo_tables(conn: sqlite3.Connection) -> None:
def seed_customers(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
def seed_orders(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
def join_customers_with_paid_orders(conn: sqlite3.Connection) -> list[str]:
def join_distinct_customers_with_paid_orders(conn: sqlite3.Connection) -> list[str]:
def subquery_customers_with_paid_orders(conn: sqlite3.Connection) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/relational/join-vs-subquery-shapes/python -q
```

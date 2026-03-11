# Semi-Join And Anti-Join Shapes

> Track: `databases` | Topic: `relational`

## Concept

Semi-joins keep left-side rows that have a match. Anti-joins keep left-side rows that do not have a match.

## Key Points

- A semi-join answers “which left-side rows have at least one match?”
- An anti-join answers “which left-side rows have no match?”
- Both shapes return left-side rows, not one row per matching pair.
- These shapes often map better to existence questions than raw joins.

## Minimal Code Mental Model

```python
conn = create_connection()
create_demo_tables(conn)
seed_customers(conn, [(1, "Ada"), (2, "Linus"), (3, "Grace")])
seed_orders(conn, [(1, "paid"), (1, "paid"), (2, "draft")])
semi = semi_join_customers_with_paid_orders(conn)
anti = anti_join_customers_without_paid_orders(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_demo_tables(conn: sqlite3.Connection) -> None:
def seed_customers(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
def seed_orders(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
def inner_join_paid_order_names(conn: sqlite3.Connection) -> list[str]:
def semi_join_customers_with_paid_orders(conn: sqlite3.Connection) -> list[str]:
def anti_join_customers_without_paid_orders(conn: sqlite3.Connection) -> list[str]:
```

## Run tests

```bash
pytest modules/databases/relational/semi-join-and-anti-join-shapes/python -q
```

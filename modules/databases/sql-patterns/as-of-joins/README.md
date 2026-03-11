# As Of Joins

> Track: `databases` | Topic: `sql-patterns`

## Concept

An as-of join matches each fact row to the latest dimension version that existed at that time. It is the standard pattern for temporal pricing, slowly changing metadata, and historical attribution.

## Key Points

- The join condition is “latest row where `effective_at <= event_time`”.
- Regular joins on the current dimension state can rewrite history by attaching newer values to older events.
- This matters for revenue, experiments, model config history, and compliance trails.
- ISO-style timestamps make simple SQLite demos possible because lexical order matches time order.

## Minimal Code Mental Model

```python
insert_price(conn, "A", "2026-01-01", 100)
insert_sale(conn, "A", "2026-01-15", 2)
rows = as_of_sale_prices(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_as_of_join_tables(conn: sqlite3.Connection) -> None:
def insert_price(conn: sqlite3.Connection, sku: str, effective_at: str, price_cents: int) -> int:
def insert_sale(conn: sqlite3.Connection, sku: str, sold_at: str, quantity: int) -> int:
def as_of_sale_prices(conn: sqlite3.Connection) -> list[tuple[int, str, str, int, int]]:
def revenue_as_of_sale_time(conn: sqlite3.Connection) -> int:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/as-of-joins/python -q
```

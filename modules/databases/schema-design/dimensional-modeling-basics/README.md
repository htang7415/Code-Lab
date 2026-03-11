# Dimensional Modeling Basics

> Track: `databases` | Topic: `schema-design`

## Concept

A dimensional model separates descriptive dimensions from numeric facts so analytics queries can aggregate quickly and stay easy to reason about.

## Key Points

- Fact tables store events or measurements at a clear grain.
- Dimension tables store reusable descriptive attributes like product, tenant, or calendar date.
- A star schema keeps analytics joins predictable: fact in the middle, dimensions around it.
- This pattern is still common in 2026 analytics stacks even when the storage layer is Parquet or a lakehouse engine.

## Minimal Code Mental Model

```python
conn = create_connection()
create_star_schema(conn)
product_id = insert_product(conn, "BOOK-1", "books")
date_id = insert_calendar_date(conn, "2026-01-01")
insert_sale(conn, product_id, date_id, 500)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_star_schema(conn: sqlite3.Connection) -> None:
def insert_product(conn: sqlite3.Connection, sku: str, category: str) -> int:
def insert_calendar_date(conn: sqlite3.Connection, day: str) -> int:
def insert_sale(
    conn: sqlite3.Connection,
    product_id: int,
    date_id: int,
    amount_cents: int,
) -> None:
def revenue_by_category(conn: sqlite3.Connection) -> list[tuple[str, int]]:
def sales_by_day(conn: sqlite3.Connection) -> list[tuple[str, int]]:
```

## Run tests

```bash
pytest modules/databases/schema-design/dimensional-modeling-basics/python -q
```

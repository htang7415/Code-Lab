# Fact Grain And Double Counting

> Track: `databases` | Topic: `schema-design`

## Concept

Fact grain is the exact thing one row represents. If you aggregate a fact table at order grain after joining to line items, you can count the same order multiple times.

## Key Points

- Every fact table needs one unambiguous row grain: one order, one event, one click, one chunk, and so on.
- Joining a coarse-grain fact to a finer-grain table multiplies rows unless the query compensates for it.
- Many analytics bugs are not syntax bugs. They are grain bugs.
- In AI systems this shows up when document-level metrics get joined to chunk-level or span-level tables.

## Minimal Code Mental Model

```python
conn = create_connection()
create_order_item_schema(conn)
order_id = insert_order(conn, 1000)
insert_order_item(conn, order_id, "A", 1)
correct = correct_total_from_order_grain(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_order_item_schema(conn: sqlite3.Connection) -> None:
def insert_order(conn: sqlite3.Connection, order_total_cents: int) -> int:
def insert_order_item(conn: sqlite3.Connection, order_id: int, sku: str, quantity: int) -> int:
def correct_total_from_order_grain(conn: sqlite3.Connection) -> int:
def duplicated_total_from_item_join(conn: sqlite3.Connection) -> int:
def item_counts_by_order(conn: sqlite3.Connection) -> list[tuple[int, int]]:
```

## Run tests

```bash
pytest modules/databases/schema-design/fact-grain-and-double-counting/python -q
```

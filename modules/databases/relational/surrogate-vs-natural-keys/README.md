# Surrogate Vs Natural Keys

> Track: `databases` | Topic: `relational`

## Concept

Natural keys come from real business fields like email or SKU. Surrogate keys are stable internal IDs. When business fields can change, surrogate keys keep child tables from inheriting that churn.

## Key Points

- Natural keys can be useful when the business identifier is truly stable and already unique.
- Mutable natural keys create update fanout because child rows may also need to change.
- Surrogate keys keep relationships stable while business fields stay as ordinary unique columns.
- In AI products, document URIs, model names, and user emails often behave like mutable business identifiers, not ideal primary keys.

## Minimal Code Mental Model

```python
conn = create_connection()
create_key_strategy_schema(conn)
insert_natural_customer(conn, "a@example.com", "Alice")
insert_natural_order(conn, "a@example.com", "n-1")
fanout = natural_key_write_fanout(conn, "a@example.com")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_key_strategy_schema(conn: sqlite3.Connection) -> None:
def insert_natural_customer(conn: sqlite3.Connection, email: str, display_name: str) -> None:
def insert_natural_order(conn: sqlite3.Connection, customer_email: str, order_code: str) -> int:
def insert_surrogate_customer(conn: sqlite3.Connection, email: str, display_name: str) -> int:
def insert_surrogate_order(conn: sqlite3.Connection, customer_id: int, order_code: str) -> int:
def natural_key_write_fanout(conn: sqlite3.Connection, customer_email: str) -> int:
def surrogate_key_write_fanout(conn: sqlite3.Connection, customer_id: int) -> int:
def rename_natural_customer_email(conn: sqlite3.Connection, old_email: str, new_email: str) -> None:
def rename_surrogate_customer_email(conn: sqlite3.Connection, customer_id: int, new_email: str) -> None:
```

## Run tests

```bash
pytest modules/databases/relational/surrogate-vs-natural-keys/python -q
```

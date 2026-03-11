# Outbox Pattern

> Track: `databases` | Topic: `transactions`

## Concept

The outbox pattern writes domain state and the event to publish in the same transaction so they cannot drift apart.

## Key Points

- A domain write without its event can silently break downstream systems.
- An event without the domain write can publish a lie.
- The outbox table is a durable handoff between transactional writes and asynchronous delivery.
- Publishing usually becomes a second step that reads pending outbox rows and marks them sent.

## Minimal Code Mental Model

```python
conn = create_connection()
create_order_outbox_tables(conn)
order_id = create_order_with_outbox(conn, customer_id="cust-1", status="placed")
events = pending_outbox_events(conn)
mark_event_published(conn, events[0][0], "2026-03-11T10:05:00Z")
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_order_outbox_tables(conn: sqlite3.Connection) -> None:
def create_order_with_outbox(
    conn: sqlite3.Connection,
    customer_id: str,
    status: str,
    fail_after_order: bool = False,
) -> int:
def pending_outbox_events(
    conn: sqlite3.Connection,
) -> list[tuple[int, str, int, str]]:
def order_rows(conn: sqlite3.Connection) -> list[tuple[int, str, str]]:
def mark_event_published(
    conn: sqlite3.Connection,
    event_id: int,
    published_at: str,
) -> None:
```

## Run tests

```bash
pytest modules/databases/transactions/outbox-pattern/python -q
```

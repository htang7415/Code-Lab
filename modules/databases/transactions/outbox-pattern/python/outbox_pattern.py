"""outbox_pattern - atomic domain writes plus durable outbound events."""

from __future__ import annotations

import json
import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.isolation_level = None
    return conn


def create_order_outbox_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id TEXT NOT NULL,
            status TEXT NOT NULL
        );

        CREATE TABLE outbox (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            aggregate_type TEXT NOT NULL,
            aggregate_id INTEGER NOT NULL,
            event_name TEXT NOT NULL,
            payload_json TEXT NOT NULL,
            published_at TEXT
        );
        """
    )


def create_order_with_outbox(
    conn: sqlite3.Connection,
    customer_id: str,
    status: str,
    fail_after_order: bool = False,
) -> int:
    conn.execute("BEGIN")
    try:
        order_cursor = conn.execute(
            """
            INSERT INTO orders (customer_id, status)
            VALUES (?, ?)
            """,
            (customer_id, status),
        )
        order_id = int(order_cursor.lastrowid)

        if fail_after_order:
            raise RuntimeError("simulated failure before writing outbox")

        payload = json.dumps({"customer_id": customer_id, "status": status})
        conn.execute(
            """
            INSERT INTO outbox (aggregate_type, aggregate_id, event_name, payload_json)
            VALUES ('order', ?, 'order.created', ?)
            """,
            (order_id, payload),
        )
        conn.execute("COMMIT")
        return order_id
    except Exception:
        conn.execute("ROLLBACK")
        raise


def pending_outbox_events(
    conn: sqlite3.Connection,
) -> list[tuple[int, str, int, str]]:
    rows = conn.execute(
        """
        SELECT id, aggregate_type, aggregate_id, event_name
        FROM outbox
        WHERE published_at IS NULL
        ORDER BY id
        """
    ).fetchall()
    return [(event_id, aggregate_type, aggregate_id, event_name) for event_id, aggregate_type, aggregate_id, event_name in rows]


def order_rows(conn: sqlite3.Connection) -> list[tuple[int, str, str]]:
    rows = conn.execute(
        """
        SELECT id, customer_id, status
        FROM orders
        ORDER BY id
        """
    ).fetchall()
    return [(order_id, customer_id, status) for order_id, customer_id, status in rows]


def mark_event_published(
    conn: sqlite3.Connection,
    event_id: int,
    published_at: str,
) -> None:
    conn.execute(
        """
        UPDATE outbox
        SET published_at = ?
        WHERE id = ?
        """,
        (published_at, event_id),
    )

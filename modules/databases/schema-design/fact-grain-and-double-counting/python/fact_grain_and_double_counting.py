"""fact_grain_and_double_counting - grain mistakes that inflate aggregates."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_order_item_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_total_cents INTEGER NOT NULL
        );

        CREATE TABLE order_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id INTEGER NOT NULL,
            sku TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE
        );
        """
    )


def insert_order(conn: sqlite3.Connection, order_total_cents: int) -> int:
    cursor = conn.execute(
        """
        INSERT INTO orders (order_total_cents)
        VALUES (?)
        """,
        (order_total_cents,),
    )
    return int(cursor.lastrowid)


def insert_order_item(
    conn: sqlite3.Connection,
    order_id: int,
    sku: str,
    quantity: int,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO order_items (order_id, sku, quantity)
        VALUES (?, ?, ?)
        """,
        (order_id, sku, quantity),
    )
    return int(cursor.lastrowid)


def correct_total_from_order_grain(conn: sqlite3.Connection) -> int:
    row = conn.execute("SELECT COALESCE(SUM(order_total_cents), 0) FROM orders").fetchone()
    assert row is not None
    return int(row[0])


def duplicated_total_from_item_join(conn: sqlite3.Connection) -> int:
    row = conn.execute(
        """
        SELECT COALESCE(SUM(o.order_total_cents), 0)
        FROM orders AS o
        JOIN order_items AS i ON i.order_id = o.id
        """
    ).fetchone()
    assert row is not None
    return int(row[0])


def item_counts_by_order(conn: sqlite3.Connection) -> list[tuple[int, int]]:
    rows = conn.execute(
        """
        SELECT order_id, COUNT(*) AS item_count
        FROM order_items
        GROUP BY order_id
        ORDER BY order_id
        """
    ).fetchall()
    return [(int(order_id), int(item_count)) for order_id, item_count in rows]

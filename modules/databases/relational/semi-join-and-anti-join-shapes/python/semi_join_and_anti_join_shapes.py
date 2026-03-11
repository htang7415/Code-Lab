"""semi_join_and_anti_join_shapes - compare existence-based join shapes with raw joins."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_demo_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE customers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );

        CREATE TABLE orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            status TEXT NOT NULL
        );
        """
    )


def seed_customers(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
    conn.executemany("INSERT INTO customers (id, name) VALUES (?, ?)", rows)


def seed_orders(conn: sqlite3.Connection, rows: list[tuple[int, str]]) -> None:
    conn.executemany(
        "INSERT INTO orders (customer_id, status) VALUES (?, ?)",
        rows,
    )


def inner_join_paid_order_names(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute(
        """
        SELECT c.name
        FROM customers AS c
        JOIN orders AS o
          ON o.customer_id = c.id
        WHERE o.status = 'paid'
        ORDER BY c.id, o.id
        """
    ).fetchall()
    return [name for (name,) in rows]


def semi_join_customers_with_paid_orders(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute(
        """
        SELECT c.name
        FROM customers AS c
        WHERE EXISTS (
            SELECT 1
            FROM orders AS o
            WHERE o.customer_id = c.id
              AND o.status = 'paid'
        )
        ORDER BY c.id
        """
    ).fetchall()
    return [name for (name,) in rows]


def anti_join_customers_without_paid_orders(conn: sqlite3.Connection) -> list[str]:
    rows = conn.execute(
        """
        SELECT c.name
        FROM customers AS c
        WHERE NOT EXISTS (
            SELECT 1
            FROM orders AS o
            WHERE o.customer_id = c.id
              AND o.status = 'paid'
        )
        ORDER BY c.id
        """
    ).fetchall()
    return [name for (name,) in rows]

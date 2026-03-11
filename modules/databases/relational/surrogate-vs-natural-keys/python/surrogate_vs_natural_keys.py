"""surrogate_vs_natural_keys - stable internal IDs versus mutable business keys."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_key_strategy_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE natural_customers (
            email TEXT PRIMARY KEY,
            display_name TEXT NOT NULL
        );

        CREATE TABLE natural_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_email TEXT NOT NULL,
            order_code TEXT NOT NULL UNIQUE,
            FOREIGN KEY (customer_email) REFERENCES natural_customers(email)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        );

        CREATE TABLE surrogate_customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            display_name TEXT NOT NULL
        );

        CREATE TABLE surrogate_orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            order_code TEXT NOT NULL UNIQUE,
            FOREIGN KEY (customer_id) REFERENCES surrogate_customers(id)
                ON DELETE CASCADE
        );
        """
    )


def insert_natural_customer(
    conn: sqlite3.Connection,
    email: str,
    display_name: str,
) -> None:
    conn.execute(
        """
        INSERT INTO natural_customers (email, display_name)
        VALUES (?, ?)
        """,
        (email, display_name),
    )


def insert_natural_order(
    conn: sqlite3.Connection,
    customer_email: str,
    order_code: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO natural_orders (customer_email, order_code)
        VALUES (?, ?)
        """,
        (customer_email, order_code),
    )
    return int(cursor.lastrowid)


def insert_surrogate_customer(
    conn: sqlite3.Connection,
    email: str,
    display_name: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO surrogate_customers (email, display_name)
        VALUES (?, ?)
        """,
        (email, display_name),
    )
    return int(cursor.lastrowid)


def insert_surrogate_order(
    conn: sqlite3.Connection,
    customer_id: int,
    order_code: str,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO surrogate_orders (customer_id, order_code)
        VALUES (?, ?)
        """,
        (customer_id, order_code),
    )
    return int(cursor.lastrowid)


def natural_key_write_fanout(conn: sqlite3.Connection, customer_email: str) -> int:
    row = conn.execute(
        """
        SELECT COUNT(*)
        FROM natural_orders
        WHERE customer_email = ?
        """,
        (customer_email,),
    ).fetchone()
    assert row is not None
    return 1 + int(row[0])


def surrogate_key_write_fanout(conn: sqlite3.Connection, customer_id: int) -> int:
    row = conn.execute(
        """
        SELECT COUNT(*)
        FROM surrogate_customers
        WHERE id = ?
        """,
        (customer_id,),
    ).fetchone()
    assert row is not None
    return 1 if int(row[0]) == 1 else 0


def rename_natural_customer_email(
    conn: sqlite3.Connection,
    old_email: str,
    new_email: str,
) -> None:
    conn.execute(
        """
        UPDATE natural_customers
        SET email = ?
        WHERE email = ?
        """,
        (new_email, old_email),
    )


def rename_surrogate_customer_email(
    conn: sqlite3.Connection,
    customer_id: int,
    new_email: str,
) -> None:
    conn.execute(
        """
        UPDATE surrogate_customers
        SET email = ?
        WHERE id = ?
        """,
        (new_email, customer_id),
    )


def natural_order_rows(conn: sqlite3.Connection) -> list[tuple[str, str]]:
    rows = conn.execute(
        """
        SELECT customer_email, order_code
        FROM natural_orders
        ORDER BY id
        """
    ).fetchall()
    return [(customer_email, order_code) for customer_email, order_code in rows]


def surrogate_order_rows(conn: sqlite3.Connection) -> list[tuple[int, str]]:
    rows = conn.execute(
        """
        SELECT customer_id, order_code
        FROM surrogate_orders
        ORDER BY id
        """
    ).fetchall()
    return [(int(customer_id), order_code) for customer_id, order_code in rows]

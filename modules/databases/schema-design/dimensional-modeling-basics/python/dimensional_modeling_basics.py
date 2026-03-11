"""dimensional_modeling_basics - build a small star schema for analytics."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def create_star_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE product_dim (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT NOT NULL UNIQUE,
            category TEXT NOT NULL
        );

        CREATE TABLE date_dim (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day TEXT NOT NULL UNIQUE
        );

        CREATE TABLE sales_fact (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER NOT NULL,
            date_id INTEGER NOT NULL,
            amount_cents INTEGER NOT NULL,
            FOREIGN KEY (product_id) REFERENCES product_dim(id),
            FOREIGN KEY (date_id) REFERENCES date_dim(id)
        );
        """
    )


def insert_product(conn: sqlite3.Connection, sku: str, category: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO product_dim (sku, category)
        VALUES (?, ?)
        """,
        (sku, category),
    )
    return int(cursor.lastrowid)


def insert_calendar_date(conn: sqlite3.Connection, day: str) -> int:
    cursor = conn.execute(
        """
        INSERT INTO date_dim (day)
        VALUES (?)
        """,
        (day,),
    )
    return int(cursor.lastrowid)


def insert_sale(
    conn: sqlite3.Connection,
    product_id: int,
    date_id: int,
    amount_cents: int,
) -> None:
    conn.execute(
        """
        INSERT INTO sales_fact (product_id, date_id, amount_cents)
        VALUES (?, ?, ?)
        """,
        (product_id, date_id, amount_cents),
    )


def revenue_by_category(conn: sqlite3.Connection) -> list[tuple[str, int]]:
    rows = conn.execute(
        """
        SELECT p.category, SUM(f.amount_cents) AS revenue_cents
        FROM sales_fact AS f
        JOIN product_dim AS p ON p.id = f.product_id
        GROUP BY p.category
        ORDER BY p.category
        """
    ).fetchall()
    return [(category, int(revenue)) for category, revenue in rows]


def sales_by_day(conn: sqlite3.Connection) -> list[tuple[str, int]]:
    rows = conn.execute(
        """
        SELECT d.day, SUM(f.amount_cents) AS revenue_cents
        FROM sales_fact AS f
        JOIN date_dim AS d ON d.id = f.date_id
        GROUP BY d.day
        ORDER BY d.day
        """
    ).fetchall()
    return [(day, int(revenue)) for day, revenue in rows]

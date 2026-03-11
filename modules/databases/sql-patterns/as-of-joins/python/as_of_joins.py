"""as_of_joins - join a fact row to the latest prior dimension version."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    return sqlite3.connect(":memory:")


def create_as_of_join_tables(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT NOT NULL,
            effective_at TEXT NOT NULL,
            price_cents INTEGER NOT NULL
        );

        CREATE TABLE sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT NOT NULL,
            sold_at TEXT NOT NULL,
            quantity INTEGER NOT NULL
        );
        """
    )


def insert_price(
    conn: sqlite3.Connection,
    sku: str,
    effective_at: str,
    price_cents: int,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO price_history (sku, effective_at, price_cents)
        VALUES (?, ?, ?)
        """,
        (sku, effective_at, price_cents),
    )
    return int(cursor.lastrowid)


def insert_sale(
    conn: sqlite3.Connection,
    sku: str,
    sold_at: str,
    quantity: int,
) -> int:
    cursor = conn.execute(
        """
        INSERT INTO sales (sku, sold_at, quantity)
        VALUES (?, ?, ?)
        """,
        (sku, sold_at, quantity),
    )
    return int(cursor.lastrowid)


def as_of_sale_prices(conn: sqlite3.Connection) -> list[tuple[int, str, str, int, int]]:
    rows = conn.execute(
        """
        SELECT
            s.id,
            s.sku,
            s.sold_at,
            p.price_cents,
            s.quantity
        FROM sales AS s
        JOIN price_history AS p
          ON p.sku = s.sku
         AND p.effective_at = (
            SELECT MAX(p2.effective_at)
            FROM price_history AS p2
            WHERE p2.sku = s.sku
              AND p2.effective_at <= s.sold_at
         )
        ORDER BY s.id
        """
    ).fetchall()
    return [
        (int(sale_id), sku, sold_at, int(price_cents), int(quantity))
        for sale_id, sku, sold_at, price_cents, quantity in rows
    ]


def revenue_as_of_sale_time(conn: sqlite3.Connection) -> int:
    return sum(price_cents * quantity for _, _, _, price_cents, quantity in as_of_sale_prices(conn))

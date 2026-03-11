"""transaction_basics - atomic multi-step updates with rollback."""

from __future__ import annotations

import sqlite3


def create_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.isolation_level = None
    return conn


def create_accounts_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner TEXT NOT NULL UNIQUE,
            balance INTEGER NOT NULL CHECK (balance >= 0)
        )
        """
    )


def create_account(conn: sqlite3.Connection, owner: str, balance: int) -> int:
    cursor = conn.execute(
        "INSERT INTO accounts (owner, balance) VALUES (?, ?)",
        (owner, balance),
    )
    return int(cursor.lastrowid)


def account_balances(conn: sqlite3.Connection) -> dict[str, int]:
    rows = conn.execute(
        "SELECT owner, balance FROM accounts ORDER BY owner"
    ).fetchall()
    return {owner: balance for owner, balance in rows}


def transfer_funds(
    conn: sqlite3.Connection,
    from_account_id: int,
    to_account_id: int,
    amount: int,
    fail_after_debit: bool = False,
) -> None:
    if amount <= 0:
        raise ValueError("amount must be positive")

    conn.execute("BEGIN")
    try:
        debit = conn.execute(
            """
            UPDATE accounts
            SET balance = balance - ?
            WHERE id = ? AND balance >= ?
            """,
            (amount, from_account_id, amount),
        )
        if debit.rowcount != 1:
            raise ValueError("insufficient funds or missing source account")

        if fail_after_debit:
            raise RuntimeError("simulated failure after debit")

        credit = conn.execute(
            """
            UPDATE accounts
            SET balance = balance + ?
            WHERE id = ?
            """,
            (amount, to_account_id),
        )
        if credit.rowcount != 1:
            raise ValueError("missing destination account")

        conn.execute("COMMIT")
    except Exception:
        conn.execute("ROLLBACK")
        raise

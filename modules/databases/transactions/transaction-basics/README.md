# Transaction Basics

> Track: `databases` | Topic: `transactions`

## Concept

A transaction groups several writes so they either all happen or none of them do.

## Key Points

- Transactions protect multi-step updates like money movement or job state transitions.
- Rollback is the core recovery mechanism when a failure happens in the middle.
- Constraints and transactions work together: constraints reject invalid states, transactions keep partial work from leaking.
- Atomicity matters in AI systems too, especially for billing, job orchestration, and status updates.

## Minimal Code Mental Model

```python
conn = create_connection()
create_accounts_table(conn)
from_id = create_account(conn, "ops", 150)
to_id = create_account(conn, "research", 20)
transfer_funds(conn, from_id, to_id, 50)
balances = account_balances(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_accounts_table(conn: sqlite3.Connection) -> None:
def create_account(conn: sqlite3.Connection, owner: str, balance: int) -> int:
def account_balances(conn: sqlite3.Connection) -> dict[str, int]:
def transfer_funds(
    conn: sqlite3.Connection,
    from_account_id: int,
    to_account_id: int,
    amount: int,
    fail_after_debit: bool = False,
) -> None:
```

## Run tests

```bash
pytest modules/databases/transactions/transaction-basics/python -q
```

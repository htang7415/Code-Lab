# Cohort Retention Basics

> Track: `databases` | Topic: `sql-patterns`

## Concept

Cohort retention groups users by their starting month, then measures how many of them come back in later periods. The core SQL pattern is a join between cohort membership and later activity with a computed month age.

## Key Points

- Cohort size is the denominator.
- Retained users in month `n` are the numerator.
- Retention analysis depends on distinct active users, not raw event counts.
- This pattern shows up in product analytics, dataset refresh usage, and agent workspace engagement.

## Minimal Code Mental Model

```python
insert_user(conn, "u1", "2026-01")
insert_activity(conn, "u1", "2026-02")
rates = retention_rates(conn)
```

## Function

```python
def create_connection() -> sqlite3.Connection:
def create_retention_schema(conn: sqlite3.Connection) -> None:
def insert_user(conn: sqlite3.Connection, user_id: str, cohort_month: str) -> None:
def insert_activity(conn: sqlite3.Connection, user_id: str, activity_month: str) -> None:
def cohort_sizes(conn: sqlite3.Connection) -> list[tuple[str, int]]:
def retained_users_by_period(conn: sqlite3.Connection) -> list[tuple[str, int, int]]:
def retention_rates(conn: sqlite3.Connection) -> list[tuple[str, int, float]]:
```

## Run tests

```bash
pytest modules/databases/sql-patterns/cohort-retention-basics/python -q
```

from cohort_retention_basics import (
    cohort_sizes,
    create_connection,
    create_retention_schema,
    insert_activity,
    insert_user,
    retained_users_by_period,
    retention_rates,
)


def test_cohort_sizes_and_retained_users_by_month_age() -> None:
    conn = create_connection()
    create_retention_schema(conn)

    insert_user(conn, "u1", "2026-01")
    insert_user(conn, "u2", "2026-01")
    insert_user(conn, "u3", "2026-02")

    insert_activity(conn, "u1", "2026-01")
    insert_activity(conn, "u1", "2026-02")
    insert_activity(conn, "u2", "2026-01")
    insert_activity(conn, "u3", "2026-02")
    insert_activity(conn, "u3", "2026-03")

    assert cohort_sizes(conn) == [("2026-01", 2), ("2026-02", 1)]
    assert retained_users_by_period(conn) == [
        ("2026-01", 0, 2),
        ("2026-01", 1, 1),
        ("2026-02", 0, 1),
        ("2026-02", 1, 1),
    ]


def test_retention_rates_normalize_by_cohort_size() -> None:
    conn = create_connection()
    create_retention_schema(conn)

    insert_user(conn, "u1", "2026-01")
    insert_user(conn, "u2", "2026-01")
    insert_user(conn, "u3", "2026-02")

    insert_activity(conn, "u1", "2026-01")
    insert_activity(conn, "u1", "2026-02")
    insert_activity(conn, "u2", "2026-01")
    insert_activity(conn, "u3", "2026-02")
    insert_activity(conn, "u3", "2026-03")

    assert retention_rates(conn) == [
        ("2026-01", 0, 1.0),
        ("2026-01", 1, 0.5),
        ("2026-02", 0, 1.0),
        ("2026-02", 1, 1.0),
    ]

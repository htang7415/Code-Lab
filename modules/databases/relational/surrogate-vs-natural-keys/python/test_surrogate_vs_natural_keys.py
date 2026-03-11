from surrogate_vs_natural_keys import (
    create_connection,
    create_key_strategy_schema,
    insert_natural_customer,
    insert_natural_order,
    insert_surrogate_customer,
    insert_surrogate_order,
    natural_key_write_fanout,
    natural_order_rows,
    rename_natural_customer_email,
    rename_surrogate_customer_email,
    surrogate_key_write_fanout,
    surrogate_order_rows,
)


def test_natural_keys_create_update_fanout_across_child_rows() -> None:
    conn = create_connection()
    create_key_strategy_schema(conn)

    insert_natural_customer(conn, "a@example.com", "Alice")
    for code in ["n-1", "n-2", "n-3"]:
        insert_natural_order(conn, "a@example.com", code)

    assert natural_key_write_fanout(conn, "a@example.com") == 4

    rename_natural_customer_email(conn, "a@example.com", "alice@example.com")

    assert natural_order_rows(conn) == [
        ("alice@example.com", "n-1"),
        ("alice@example.com", "n-2"),
        ("alice@example.com", "n-3"),
    ]


def test_surrogate_keys_keep_child_rows_stable_when_email_changes() -> None:
    conn = create_connection()
    create_key_strategy_schema(conn)

    customer_id = insert_surrogate_customer(conn, "b@example.com", "Bob")
    for code in ["s-1", "s-2", "s-3"]:
        insert_surrogate_order(conn, customer_id, code)

    assert surrogate_key_write_fanout(conn, customer_id) == 1

    rename_surrogate_customer_email(conn, customer_id, "bob@example.com")

    assert surrogate_order_rows(conn) == [
        (customer_id, "s-1"),
        (customer_id, "s-2"),
        (customer_id, "s-3"),
    ]

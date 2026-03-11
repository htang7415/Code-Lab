from semi_join_and_anti_join_shapes import (
    anti_join_customers_without_paid_orders,
    create_connection,
    create_demo_tables,
    inner_join_paid_order_names,
    seed_customers,
    seed_orders,
    semi_join_customers_with_paid_orders,
)


def test_semi_join_returns_one_row_per_matching_left_row():
    conn = create_connection()
    create_demo_tables(conn)
    seed_customers(conn, [(1, "Ada"), (2, "Linus"), (3, "Grace")])
    seed_orders(conn, [(1, "paid"), (1, "paid"), (2, "draft"), (3, "paid")])

    assert inner_join_paid_order_names(conn) == ["Ada", "Ada", "Grace"]
    assert semi_join_customers_with_paid_orders(conn) == ["Ada", "Grace"]


def test_anti_join_finds_left_rows_with_no_paid_match():
    conn = create_connection()
    create_demo_tables(conn)
    seed_customers(conn, [(1, "Ada"), (2, "Linus"), (3, "Grace")])
    seed_orders(conn, [(1, "paid"), (2, "draft")])

    assert anti_join_customers_without_paid_orders(conn) == ["Linus", "Grace"]

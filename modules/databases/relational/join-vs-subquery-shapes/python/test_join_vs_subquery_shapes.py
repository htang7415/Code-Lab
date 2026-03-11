from join_vs_subquery_shapes import (
    create_connection,
    create_demo_tables,
    join_customers_with_paid_orders,
    join_distinct_customers_with_paid_orders,
    seed_customers,
    seed_orders,
    subquery_customers_with_paid_orders,
)


def test_join_shape_duplicates_customers_with_multiple_paid_orders():
    conn = create_connection()
    create_demo_tables(conn)
    seed_customers(conn, [(1, "Ada"), (2, "Linus")])
    seed_orders(conn, [(1, "paid"), (1, "paid"), (2, "draft")])

    assert join_customers_with_paid_orders(conn) == ["Ada", "Ada"]


def test_exists_subquery_returns_one_row_per_matching_customer():
    conn = create_connection()
    create_demo_tables(conn)
    seed_customers(conn, [(1, "Ada"), (2, "Linus"), (3, "Grace")])
    seed_orders(conn, [(1, "paid"), (1, "paid"), (2, "draft"), (3, "paid")])

    assert subquery_customers_with_paid_orders(conn) == ["Ada", "Grace"]
    assert join_distinct_customers_with_paid_orders(conn) == ["Ada", "Grace"]

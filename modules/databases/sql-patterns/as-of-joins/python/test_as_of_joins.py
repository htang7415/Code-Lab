from as_of_joins import (
    as_of_sale_prices,
    create_as_of_join_tables,
    create_connection,
    insert_price,
    insert_sale,
    revenue_as_of_sale_time,
)


def test_as_of_join_uses_latest_price_not_after_the_sale() -> None:
    conn = create_connection()
    create_as_of_join_tables(conn)

    insert_price(conn, "A", "2026-01-01", 100)
    insert_price(conn, "A", "2026-02-01", 130)
    insert_price(conn, "B", "2026-01-01", 50)

    sale_1 = insert_sale(conn, "A", "2026-01-15", 2)
    sale_2 = insert_sale(conn, "A", "2026-02-10", 1)
    sale_3 = insert_sale(conn, "B", "2026-01-20", 3)

    assert as_of_sale_prices(conn) == [
        (sale_1, "A", "2026-01-15", 100, 2),
        (sale_2, "A", "2026-02-10", 130, 1),
        (sale_3, "B", "2026-01-20", 50, 3),
    ]
    assert revenue_as_of_sale_time(conn) == 480


def test_sales_before_the_first_known_version_are_excluded() -> None:
    conn = create_connection()
    create_as_of_join_tables(conn)

    insert_price(conn, "A", "2026-01-01", 100)
    insert_sale(conn, "A", "2025-12-31", 2)
    sale_id = insert_sale(conn, "A", "2026-01-02", 1)

    assert as_of_sale_prices(conn) == [
        (sale_id, "A", "2026-01-02", 100, 1),
    ]

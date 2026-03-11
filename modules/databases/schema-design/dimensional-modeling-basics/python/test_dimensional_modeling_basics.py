from dimensional_modeling_basics import (
    create_connection,
    create_star_schema,
    insert_calendar_date,
    insert_product,
    insert_sale,
    revenue_by_category,
    sales_by_day,
)


def test_revenue_by_category_rolls_up_fact_rows() -> None:
    conn = create_connection()
    create_star_schema(conn)

    books = insert_product(conn, "BOOK-1", "books")
    tools = insert_product(conn, "TOOL-1", "tools")
    jan_1 = insert_calendar_date(conn, "2026-01-01")
    jan_2 = insert_calendar_date(conn, "2026-01-02")

    insert_sale(conn, books, jan_1, 500)
    insert_sale(conn, books, jan_2, 700)
    insert_sale(conn, tools, jan_2, 900)

    assert revenue_by_category(conn) == [("books", 1200), ("tools", 900)]


def test_sales_by_day_joins_fact_to_date_dimension() -> None:
    conn = create_connection()
    create_star_schema(conn)

    product = insert_product(conn, "SKU-1", "lab")
    jan_1 = insert_calendar_date(conn, "2026-01-01")
    jan_2 = insert_calendar_date(conn, "2026-01-02")

    insert_sale(conn, product, jan_1, 300)
    insert_sale(conn, product, jan_1, 200)
    insert_sale(conn, product, jan_2, 900)

    assert sales_by_day(conn) == [("2026-01-01", 500), ("2026-01-02", 900)]

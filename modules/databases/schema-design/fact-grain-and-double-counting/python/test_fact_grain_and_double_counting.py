from fact_grain_and_double_counting import (
    correct_total_from_order_grain,
    create_connection,
    create_order_item_schema,
    duplicated_total_from_item_join,
    insert_order,
    insert_order_item,
    item_counts_by_order,
)


def test_joining_order_facts_to_items_can_double_count() -> None:
    conn = create_connection()
    create_order_item_schema(conn)

    order_1 = insert_order(conn, 1000)
    order_2 = insert_order(conn, 500)

    insert_order_item(conn, order_1, "A", 1)
    insert_order_item(conn, order_1, "B", 2)
    insert_order_item(conn, order_2, "C", 1)

    assert item_counts_by_order(conn) == [(order_1, 2), (order_2, 1)]
    assert correct_total_from_order_grain(conn) == 1500
    assert duplicated_total_from_item_join(conn) == 2500


def test_single_item_orders_do_not_inflate_the_total() -> None:
    conn = create_connection()
    create_order_item_schema(conn)

    order_1 = insert_order(conn, 800)
    order_2 = insert_order(conn, 600)
    insert_order_item(conn, order_1, "A", 1)
    insert_order_item(conn, order_2, "B", 1)

    assert correct_total_from_order_grain(conn) == 1400
    assert duplicated_total_from_item_join(conn) == 1400

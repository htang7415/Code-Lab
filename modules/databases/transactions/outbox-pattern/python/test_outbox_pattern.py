import pytest

from outbox_pattern import (
    create_connection,
    create_order_outbox_tables,
    create_order_with_outbox,
    mark_event_published,
    order_rows,
    pending_outbox_events,
)


def build_connection():
    conn = create_connection()
    create_order_outbox_tables(conn)
    return conn


def test_successful_transaction_writes_order_and_outbox_event() -> None:
    conn = build_connection()
    order_id = create_order_with_outbox(conn, customer_id="cust-1", status="placed")

    assert order_rows(conn) == [(order_id, "cust-1", "placed")]
    assert pending_outbox_events(conn) == [
        (1, "order", order_id, "order.created")
    ]


def test_failure_rolls_back_both_the_domain_row_and_the_event() -> None:
    conn = build_connection()

    with pytest.raises(RuntimeError):
        create_order_with_outbox(
            conn,
            customer_id="cust-1",
            status="placed",
            fail_after_order=True,
        )

    assert order_rows(conn) == []
    assert pending_outbox_events(conn) == []


def test_marking_event_published_removes_it_from_the_pending_queue() -> None:
    conn = build_connection()
    create_order_with_outbox(conn, customer_id="cust-1", status="placed")

    mark_event_published(conn, 1, "2026-03-11T10:05:00Z")

    assert pending_outbox_events(conn) == []

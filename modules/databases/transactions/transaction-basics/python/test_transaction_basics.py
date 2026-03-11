import pytest

from transaction_basics import (
    account_balances,
    create_account,
    create_accounts_table,
    create_connection,
    transfer_funds,
)


def build_accounts():
    conn = create_connection()
    create_accounts_table(conn)
    ops_id = create_account(conn, "ops", 150)
    research_id = create_account(conn, "research", 20)
    return conn, ops_id, research_id


def test_successful_transfer_updates_both_balances() -> None:
    conn, ops_id, research_id = build_accounts()

    transfer_funds(conn, ops_id, research_id, 50)

    assert account_balances(conn) == {"ops": 100, "research": 70}


def test_mid_transaction_failure_rolls_back_the_debit() -> None:
    conn, ops_id, research_id = build_accounts()

    with pytest.raises(RuntimeError):
        transfer_funds(conn, ops_id, research_id, 50, fail_after_debit=True)

    assert account_balances(conn) == {"ops": 150, "research": 20}


def test_insufficient_funds_keeps_balances_unchanged() -> None:
    conn, ops_id, research_id = build_accounts()

    with pytest.raises(ValueError):
        transfer_funds(conn, research_id, ops_id, 100)

    assert account_balances(conn) == {"ops": 150, "research": 20}

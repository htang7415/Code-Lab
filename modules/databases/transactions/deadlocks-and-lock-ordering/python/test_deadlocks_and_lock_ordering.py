from deadlocks_and_lock_ordering import (
    apply_canonical_order,
    canonical_lock_order,
    has_deadlock_risk,
    inversion_pairs,
)


def test_conflicting_lock_orders_create_an_inversion_pair() -> None:
    order_a = ["account:1", "account:2"]
    order_b = ["account:2", "account:1"]

    assert inversion_pairs(order_a, order_b) == [("account:1", "account:2")]
    assert has_deadlock_risk(order_a, order_b) is True


def test_one_shared_resource_is_not_enough_for_a_deadlock_cycle() -> None:
    order_a = ["account:1", "invoice:5"]
    order_b = ["account:1", "job:7"]

    assert inversion_pairs(order_a, order_b) == []
    assert has_deadlock_risk(order_a, order_b) is False


def test_canonical_order_removes_the_conflict_between_transactions() -> None:
    planned = apply_canonical_order(
        {
            "txn-a": ["account:2", "account:1", "account:2"],
            "txn-b": ["account:1", "account:2"],
        }
    )

    assert canonical_lock_order(["account:2", "account:1", "account:2"]) == [
        "account:1",
        "account:2",
    ]
    assert has_deadlock_risk(planned["txn-a"], planned["txn-b"]) is False

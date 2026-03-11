from consumer_rebalance_basics import rebalance_summary


def test_adding_a_consumer_moves_some_partitions_and_balances_load() -> None:
    summary = rebalance_summary(
        partitions=[0, 1, 2, 3, 4, 5],
        before_consumers=["a", "b"],
        after_consumers=["a", "b", "c"],
    )

    assert summary["before_load"] == {"a": 3, "b": 3}
    assert summary["after_load"] == {"a": 2, "b": 2, "c": 2}
    assert summary["moved_partitions"] == [
        (2, "a", "c"),
        (3, "b", "a"),
        (4, "a", "b"),
        (5, "b", "c"),
    ]


def test_removing_a_consumer_reassigns_its_partitions() -> None:
    summary = rebalance_summary(
        partitions=[0, 1, 2, 3],
        before_consumers=["a", "b", "c"],
        after_consumers=["a", "c"],
    )

    assert summary["moved_partitions"] == [
        (1, "b", "c"),
        (2, "c", "a"),
        (3, "a", "c"),
    ]

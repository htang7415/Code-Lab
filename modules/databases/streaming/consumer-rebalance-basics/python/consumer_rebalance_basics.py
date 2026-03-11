"""consumer_rebalance_basics - partitions move when the group membership changes."""

from __future__ import annotations


def assign_round_robin(
    partitions: list[int],
    consumers: list[str],
) -> dict[str, list[int]]:
    if not consumers:
        raise ValueError("at least one consumer is required")
    assignments = {consumer: [] for consumer in consumers}
    for index, partition in enumerate(sorted(partitions)):
        consumer = consumers[index % len(consumers)]
        assignments[consumer].append(partition)
    return assignments


def consumer_load(assignments: dict[str, list[int]]) -> dict[str, int]:
    return {consumer: len(partitions) for consumer, partitions in assignments.items()}


def moved_partitions(
    before: dict[str, list[int]],
    after: dict[str, list[int]],
) -> list[tuple[int, str | None, str | None]]:
    before_owner = {
        partition: consumer
        for consumer, partitions in before.items()
        for partition in partitions
    }
    after_owner = {
        partition: consumer
        for consumer, partitions in after.items()
        for partition in partitions
    }
    moved: list[tuple[int, str | None, str | None]] = []
    for partition in sorted(set(before_owner) | set(after_owner)):
        old_consumer = before_owner.get(partition)
        new_consumer = after_owner.get(partition)
        if old_consumer != new_consumer:
            moved.append((partition, old_consumer, new_consumer))
    return moved


def rebalance_summary(
    partitions: list[int],
    before_consumers: list[str],
    after_consumers: list[str],
) -> dict[str, object]:
    before = assign_round_robin(partitions, before_consumers)
    after = assign_round_robin(partitions, after_consumers)
    return {
        "before": before,
        "after": after,
        "moved_partitions": moved_partitions(before, after),
        "before_load": consumer_load(before),
        "after_load": consumer_load(after),
    }

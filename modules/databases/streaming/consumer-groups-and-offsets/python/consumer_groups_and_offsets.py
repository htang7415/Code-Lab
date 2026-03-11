"""consumer_groups_and_offsets - partition assignment and offset commits."""

from __future__ import annotations


def assign_partitions(
    partitions: list[int],
    consumers: list[str],
) -> dict[str, list[int]]:
    assignments = {consumer: [] for consumer in consumers}
    for index, partition in enumerate(sorted(partitions)):
        consumer = consumers[index % len(consumers)]
        assignments[consumer].append(partition)
    return assignments


def poll_group(
    stream: dict[int, list[dict[str, object]]],
    assignments: dict[str, list[int]],
    committed_offsets: dict[int, int],
    consumer_id: str,
    max_events: int | None = None,
) -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    for partition in assignments.get(consumer_id, []):
        next_offset = committed_offsets.get(partition, 0)
        for event in stream.get(partition, []):
            if int(event["offset"]) >= next_offset:
                events.append(event)
    events.sort(key=lambda event: (int(event["partition"]), int(event["offset"])))
    return events if max_events is None else events[:max_events]


def commit_offsets(
    committed_offsets: dict[int, int],
    events: list[dict[str, object]],
) -> None:
    for event in events:
        partition = int(event["partition"])
        offset = int(event["offset"])
        committed_offsets[partition] = max(committed_offsets.get(partition, 0), offset + 1)

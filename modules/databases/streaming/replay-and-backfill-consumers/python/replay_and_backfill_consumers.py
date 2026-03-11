"""replay_and_backfill_consumers - rebuild or patch state from a durable event log."""

from __future__ import annotations


def append_amount_event(
    stream: list[dict[str, object]],
    topic: str,
    key: str,
    amount: int,
) -> int:
    offset = len(stream)
    stream.append(
        {
            "offset": offset,
            "topic": topic,
            "key": key,
            "amount": amount,
        }
    )
    return offset


def consume_range(
    stream: list[dict[str, object]],
    topic: str,
    start_offset: int,
    end_offset: int | None = None,
) -> tuple[dict[str, int], int]:
    stop = len(stream) if end_offset is None else min(end_offset, len(stream))
    totals: dict[str, int] = {}
    for event in stream:
        offset = int(event["offset"])
        if offset < start_offset or offset >= stop:
            continue
        if str(event["topic"]) != topic:
            continue
        key = str(event["key"])
        totals[key] = totals.get(key, 0) + int(event["amount"])
    return totals, stop


def replay_topic(stream: list[dict[str, object]], topic: str) -> dict[str, int]:
    totals, _ = consume_range(stream, topic, start_offset=0)
    return totals


def backfill_into_state(
    state: dict[str, int],
    stream: list[dict[str, object]],
    topic: str,
    start_offset: int,
    end_offset: int,
) -> dict[str, int]:
    updated = {str(key): int(total) for key, total in state.items()}
    patch, _ = consume_range(stream, topic, start_offset, end_offset)
    for key, amount in patch.items():
        updated[key] = updated.get(key, 0) + amount
    return updated

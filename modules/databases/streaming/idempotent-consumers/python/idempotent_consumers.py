"""idempotent_consumers - apply each event ID at most once."""

from __future__ import annotations


def process_status_event(
    event: dict[str, str],
    processed_ids: set[str],
    state: dict[str, str],
) -> bool:
    event_id = event["event_id"]
    if event_id in processed_ids:
        return False

    state[event["key"]] = event["status"]
    processed_ids.add(event_id)
    return True


def consume_batch(
    events: list[dict[str, str]],
    processed_ids: set[str],
    state: dict[str, str],
) -> int:
    applied = 0
    for event in events:
        if process_status_event(event, processed_ids, state):
            applied += 1
    return applied

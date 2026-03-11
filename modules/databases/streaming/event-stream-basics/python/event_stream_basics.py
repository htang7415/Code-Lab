"""event_stream_basics - append-only offsets and simple materialization."""

from __future__ import annotations


def append_event(
    stream: list[dict[str, object]],
    topic: str,
    key: str,
    payload: dict[str, object],
) -> int:
    offset = len(stream)
    stream.append(
        {
            "offset": offset,
            "topic": topic,
            "key": key,
            "payload": payload,
        }
    )
    return offset


def read_from_offset(
    stream: list[dict[str, object]],
    offset: int,
    max_events: int | None = None,
) -> list[dict[str, object]]:
    events = [event for event in stream if int(event["offset"]) >= offset]
    return events if max_events is None else events[:max_events]


def consumer_lag(stream: list[dict[str, object]], next_offset: int) -> int:
    return max(len(stream) - next_offset, 0)


def materialize_latest_payload_by_key(
    stream: list[dict[str, object]],
    topic: str,
) -> dict[str, dict[str, object]]:
    latest: dict[str, dict[str, object]] = {}
    for event in stream:
        if event["topic"] == topic:
            latest[str(event["key"])] = dict(event["payload"])
    return latest

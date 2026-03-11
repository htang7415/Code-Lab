from event_stream_basics import (
    append_event,
    consumer_lag,
    materialize_latest_payload_by_key,
    read_from_offset,
)


def build_stream() -> list[dict[str, object]]:
    stream: list[dict[str, object]] = []
    append_event(stream, "document.ingested", "doc-1", {"status": "ready"})
    append_event(stream, "document.ingested", "doc-2", {"status": "ready"})
    append_event(stream, "document.ingested", "doc-1", {"status": "embedded"})
    return stream


def test_offsets_increase_with_each_append() -> None:
    stream: list[dict[str, object]] = []

    assert append_event(stream, "document.ingested", "doc-1", {"status": "ready"}) == 0
    assert append_event(stream, "document.ingested", "doc-2", {"status": "ready"}) == 1


def test_read_from_offset_returns_the_suffix_of_the_stream() -> None:
    stream = build_stream()

    assert read_from_offset(stream, offset=1) == [
        {
            "offset": 1,
            "topic": "document.ingested",
            "key": "doc-2",
            "payload": {"status": "ready"},
        },
        {
            "offset": 2,
            "topic": "document.ingested",
            "key": "doc-1",
            "payload": {"status": "embedded"},
        },
    ]


def test_lag_and_materialized_latest_state_follow_the_stream() -> None:
    stream = build_stream()

    assert consumer_lag(stream, next_offset=1) == 2
    assert materialize_latest_payload_by_key(stream, "document.ingested") == {
        "doc-1": {"status": "embedded"},
        "doc-2": {"status": "ready"},
    }

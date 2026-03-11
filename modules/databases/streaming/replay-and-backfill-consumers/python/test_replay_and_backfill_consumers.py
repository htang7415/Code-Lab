from replay_and_backfill_consumers import (
    append_amount_event,
    backfill_into_state,
    consume_range,
    replay_topic,
)


def test_replay_topic_rebuilds_state_from_offset_zero() -> None:
    stream: list[dict[str, object]] = []
    append_amount_event(stream, "sales", "ws-a", 5)
    append_amount_event(stream, "sales", "ws-b", 3)
    append_amount_event(stream, "sales", "ws-a", 4)
    append_amount_event(stream, "audit", "ws-a", 99)
    append_amount_event(stream, "sales", "ws-b", 7)

    assert replay_topic(stream, "sales") == {"ws-a": 9, "ws-b": 10}


def test_backfill_patches_a_missed_offset_range() -> None:
    stream: list[dict[str, object]] = []
    append_amount_event(stream, "sales", "ws-a", 5)
    append_amount_event(stream, "sales", "ws-b", 3)
    append_amount_event(stream, "sales", "ws-a", 4)
    append_amount_event(stream, "audit", "ws-a", 99)
    append_amount_event(stream, "sales", "ws-b", 7)

    partial, next_offset = consume_range(stream, "sales", start_offset=0, end_offset=2)
    assert partial == {"ws-a": 5, "ws-b": 3}
    assert next_offset == 2

    patched = backfill_into_state(partial, stream, "sales", start_offset=2, end_offset=5)
    assert patched == {"ws-a": 9, "ws-b": 10}

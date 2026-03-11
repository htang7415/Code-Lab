from idempotent_consumers import consume_batch, process_status_event


def test_duplicate_event_id_is_applied_only_once() -> None:
    processed_ids: set[str] = set()
    state: dict[str, str] = {}
    event = {"event_id": "evt-1", "key": "doc-1", "status": "embedded"}

    assert process_status_event(event, processed_ids, state) is True
    assert process_status_event(event, processed_ids, state) is False
    assert state == {"doc-1": "embedded"}


def test_batch_consumer_counts_only_newly_applied_events() -> None:
    processed_ids: set[str] = set()
    state: dict[str, str] = {}
    events = [
        {"event_id": "evt-1", "key": "doc-1", "status": "ready"},
        {"event_id": "evt-2", "key": "doc-2", "status": "ready"},
        {"event_id": "evt-1", "key": "doc-1", "status": "ready"},
    ]

    assert consume_batch(events, processed_ids, state) == 2
    assert state == {"doc-1": "ready", "doc-2": "ready"}


def test_new_event_for_same_key_can_still_advance_state() -> None:
    processed_ids: set[str] = {"evt-1"}
    state: dict[str, str] = {"doc-1": "ready"}
    events = [
        {"event_id": "evt-1", "key": "doc-1", "status": "ready"},
        {"event_id": "evt-3", "key": "doc-1", "status": "embedded"},
    ]

    assert consume_batch(events, processed_ids, state) == 1
    assert state == {"doc-1": "embedded"}

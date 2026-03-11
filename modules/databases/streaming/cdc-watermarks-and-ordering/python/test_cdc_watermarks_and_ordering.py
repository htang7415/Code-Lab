from cdc_watermarks_and_ordering import (
    cdc_event,
    current_watermark,
    empty_consumer_state,
    ingest_cdc_event,
    latest_row,
)


def test_watermark_waits_for_missing_sequence_then_applies_buffered_events():
    state = empty_consumer_state()

    assert ingest_cdc_event(state, cdc_event(1, "orders", "o1", "upsert", {"status": "placed"})) == [1]
    assert ingest_cdc_event(state, cdc_event(3, "orders", "o1", "upsert", {"status": "completed"})) == []
    assert current_watermark(state) == 1

    assert ingest_cdc_event(state, cdc_event(2, "orders", "o1", "upsert", {"status": "paid"})) == [2, 3]
    assert current_watermark(state) == 3
    assert latest_row(state, "orders", "o1") == {"status": "completed"}


def test_delete_only_applies_when_its_turn_arrives():
    state = empty_consumer_state()

    ingest_cdc_event(state, cdc_event(1, "orders", "o1", "upsert", {"status": "placed"}))
    ingest_cdc_event(state, cdc_event(3, "orders", "o1", "delete", None))
    assert latest_row(state, "orders", "o1") == {"status": "placed"}

    ingest_cdc_event(state, cdc_event(2, "orders", "o2", "upsert", {"status": "paid"}))
    assert latest_row(state, "orders", "o1") is None
    assert current_watermark(state) == 3

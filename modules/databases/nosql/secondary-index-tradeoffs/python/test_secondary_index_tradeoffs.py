from secondary_index_tradeoffs import (
    documents_by_status,
    index_updates_for_write,
    put_document,
)


def test_insert_adds_one_secondary_index_entry() -> None:
    store = {}
    status_index = {}

    touches = put_document(
        store,
        status_index,
        "job-1",
        {"status": "queued", "owner": "ops"},
    )

    assert touches == 1
    assert documents_by_status(store, status_index, "queued") == [
        {"id": "job-1", "status": "queued", "owner": "ops"},
    ]


def test_updating_an_indexed_field_requires_remove_and_add_work() -> None:
    store = {}
    status_index = {}
    put_document(store, status_index, "job-1", {"status": "queued", "owner": "ops"})

    touches = put_document(
        store,
        status_index,
        "job-1",
        {"status": "running", "owner": "ops"},
    )

    assert touches == 2
    assert documents_by_status(store, status_index, "queued") == []
    assert documents_by_status(store, status_index, "running") == [
        {"id": "job-1", "status": "running", "owner": "ops"},
    ]


def test_same_status_update_has_no_secondary_index_churn() -> None:
    assert index_updates_for_write("queued", "queued") == 0
    assert index_updates_for_write("queued", "running") == 2

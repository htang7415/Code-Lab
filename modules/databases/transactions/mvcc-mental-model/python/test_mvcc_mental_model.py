from mvcc_mental_model import (
    append_version,
    delete_visible_value,
    replace_visible_value,
    visible_value,
)


def test_older_snapshot_keeps_seeing_the_old_version_after_an_update() -> None:
    store = {}
    append_version(store, "doc-1", "draft", created_xid=10)
    replace_visible_value(store, "doc-1", "published", writer_xid=11)

    assert visible_value(store, "doc-1", snapshot_xid=10) == "draft"
    assert visible_value(store, "doc-1", snapshot_xid=11) == "published"


def test_delete_hides_a_row_only_for_newer_snapshots() -> None:
    store = {}
    append_version(store, "doc-1", "draft", created_xid=10)
    delete_visible_value(store, "doc-1", writer_xid=12)

    assert visible_value(store, "doc-1", snapshot_xid=11) == "draft"
    assert visible_value(store, "doc-1", snapshot_xid=12) is None


def test_multiple_updates_return_the_latest_visible_version_for_each_snapshot() -> None:
    store = {}
    append_version(store, "doc-1", "draft", created_xid=10)
    replace_visible_value(store, "doc-1", "review", writer_xid=11)
    replace_visible_value(store, "doc-1", "published", writer_xid=13)

    assert visible_value(store, "doc-1", snapshot_xid=10) == "draft"
    assert visible_value(store, "doc-1", snapshot_xid=12) == "review"
    assert visible_value(store, "doc-1", snapshot_xid=13) == "published"

"""secondary_index_tradeoffs - maintain a simple secondary index on document status."""

from __future__ import annotations


Store = dict[str, dict[str, object]]
StatusIndex = dict[str, set[str]]


def put_document(
    store: Store,
    status_index: StatusIndex,
    doc_id: str,
    document: dict[str, object],
) -> int:
    previous = store.get(doc_id)
    previous_status = None if previous is None else str(previous["status"])
    new_status = str(document["status"])

    if previous_status is not None and previous_status in status_index:
        status_index[previous_status].discard(doc_id)

    store[doc_id] = dict(document)
    status_index.setdefault(new_status, set()).add(doc_id)
    return index_updates_for_write(previous_status, new_status)


def documents_by_status(
    store: Store,
    status_index: StatusIndex,
    status: str,
) -> list[dict[str, object]]:
    ids = sorted(status_index.get(status, set()))
    return [dict(store[doc_id], id=doc_id) for doc_id in ids]


def index_updates_for_write(previous_status: str | None, new_status: str) -> int:
    if previous_status is None:
        return 1
    if previous_status == new_status:
        return 0
    return 2

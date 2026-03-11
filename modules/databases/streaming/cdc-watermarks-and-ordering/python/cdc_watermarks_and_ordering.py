"""cdc_watermarks_and_ordering - buffer out-of-order CDC until the watermark can advance."""

from __future__ import annotations


def cdc_event(
    sequence: int,
    table: str,
    row_id: str,
    op: str,
    after: dict[str, object] | None,
) -> dict[str, object]:
    return {
        "sequence": sequence,
        "table": table,
        "row_id": row_id,
        "op": op,
        "after": after,
    }


def empty_consumer_state() -> dict[str, object]:
    return {
        "next_sequence": 1,
        "buffer": {},
        "rows": {},
    }


def ingest_cdc_event(
    consumer_state: dict[str, object],
    event: dict[str, object],
) -> list[int]:
    next_sequence = int(consumer_state["next_sequence"])
    sequence = int(event["sequence"])
    if sequence < next_sequence:
        return []

    buffer = consumer_state["buffer"]
    assert isinstance(buffer, dict)
    buffer.setdefault(sequence, event)

    applied: list[int] = []
    rows = consumer_state["rows"]
    assert isinstance(rows, dict)
    while next_sequence in buffer:
        current = buffer.pop(next_sequence)
        key = (str(current["table"]), str(current["row_id"]))
        if current["op"] == "delete":
            rows.pop(key, None)
        else:
            rows[key] = dict(current.get("after") or {})
        applied.append(next_sequence)
        next_sequence += 1

    consumer_state["next_sequence"] = next_sequence
    return applied


def current_watermark(consumer_state: dict[str, object]) -> int:
    return int(consumer_state["next_sequence"]) - 1


def latest_row(
    consumer_state: dict[str, object],
    table: str,
    row_id: str,
) -> dict[str, object] | None:
    rows = consumer_state["rows"]
    assert isinstance(rows, dict)
    row = rows.get((table, row_id))
    return None if row is None else dict(row)

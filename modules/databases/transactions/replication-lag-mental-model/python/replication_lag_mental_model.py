"""replication_lag_mental_model - primary commit visibility versus replica replay."""

from __future__ import annotations


def empty_primary_log() -> list[dict[str, object]]:
    return []


def commit_write(
    primary_log: list[dict[str, object]],
    key: str,
    value: object | None,
) -> int:
    lsn = 1 if not primary_log else int(primary_log[-1]["lsn"]) + 1
    primary_log.append(
        {
            "lsn": lsn,
            "key": key,
            "op": "delete" if value is None else "upsert",
            "value": value,
        }
    )
    return lsn


def empty_replica_state() -> dict[str, object]:
    return {"applied_lsn": 0, "values": {}}


def apply_replica_writes(
    replica_state: dict[str, object],
    primary_log: list[dict[str, object]],
    up_to_lsn: int,
) -> list[int]:
    applied: list[int] = []
    values = replica_state["values"]
    assert isinstance(values, dict)
    current_lsn = int(replica_state["applied_lsn"])

    for entry in primary_log:
        lsn = int(entry["lsn"])
        if lsn <= current_lsn or lsn > up_to_lsn:
            continue
        key = str(entry["key"])
        if entry["op"] == "delete":
            values.pop(key, None)
        else:
            values[key] = entry["value"]
        applied.append(lsn)
        current_lsn = lsn

    replica_state["applied_lsn"] = current_lsn
    return applied


def replica_lag(
    primary_log: list[dict[str, object]],
    replica_state: dict[str, object],
) -> int:
    latest_lsn = 0 if not primary_log else int(primary_log[-1]["lsn"])
    return latest_lsn - int(replica_state["applied_lsn"])


def visible_value_on_primary(
    primary_log: list[dict[str, object]],
    key: str,
) -> object | None:
    value: object | None = None
    for entry in primary_log:
        if entry["key"] != key:
            continue
        value = None if entry["op"] == "delete" else entry["value"]
    return value


def visible_value_on_replica(
    replica_state: dict[str, object],
    key: str,
) -> object | None:
    values = replica_state["values"]
    assert isinstance(values, dict)
    return values.get(key)

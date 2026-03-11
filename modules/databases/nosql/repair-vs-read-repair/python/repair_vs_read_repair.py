"""repair_vs_read_repair - compare fixing one key on read with repairing all divergent keys."""

from __future__ import annotations


def empty_replica(name: str) -> dict[str, object]:
    return {
        "name": name,
        "data": {},
    }


def write_value(
    replica: dict[str, object],
    key: str,
    value: object,
    version: int,
) -> None:
    data = replica["data"]
    assert isinstance(data, dict)
    data[key] = {"value": value, "version": version}


def divergent_keys(
    left: dict[str, object],
    right: dict[str, object],
) -> list[str]:
    left_data = left["data"]
    right_data = right["data"]
    assert isinstance(left_data, dict)
    assert isinstance(right_data, dict)
    return sorted(
        key
        for key in set(left_data) | set(right_data)
        if left_data.get(key) != right_data.get(key)
    )


def read_with_repair(
    left: dict[str, object],
    right: dict[str, object],
    key: str,
) -> tuple[object | None, bool]:
    left_data = left["data"]
    right_data = right["data"]
    assert isinstance(left_data, dict)
    assert isinstance(right_data, dict)

    candidates = [entry for entry in [left_data.get(key), right_data.get(key)] if entry is not None]
    if not candidates:
        return None, False
    winner = max(candidates, key=lambda entry: (int(entry["version"]), str(entry["value"])))
    repaired = left_data.get(key) != winner or right_data.get(key) != winner
    left_data[key] = dict(winner)
    right_data[key] = dict(winner)
    return winner["value"], repaired


def background_repair(
    left: dict[str, object],
    right: dict[str, object],
) -> list[str]:
    repaired = divergent_keys(left, right)
    for key in repaired:
        read_with_repair(left, right, key)
    return repaired


def visible_values(replica: dict[str, object]) -> dict[str, object]:
    data = replica["data"]
    assert isinstance(data, dict)
    return {key: entry["value"] for key, entry in data.items()}

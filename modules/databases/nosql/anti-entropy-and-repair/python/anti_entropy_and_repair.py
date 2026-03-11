"""anti_entropy_and_repair - detect divergent replica keys and repair to the latest version."""

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
    data[key] = {
        "value": value,
        "version": version,
    }


def divergent_keys(
    left: dict[str, object],
    right: dict[str, object],
) -> list[str]:
    left_data = left["data"]
    right_data = right["data"]
    assert isinstance(left_data, dict)
    assert isinstance(right_data, dict)

    keys = sorted(set(left_data) | set(right_data))
    divergent: list[str] = []
    for key in keys:
        if left_data.get(key) != right_data.get(key):
            divergent.append(key)
    return divergent


def repair_pair(
    left: dict[str, object],
    right: dict[str, object],
) -> list[str]:
    left_data = left["data"]
    right_data = right["data"]
    assert isinstance(left_data, dict)
    assert isinstance(right_data, dict)

    repaired = divergent_keys(left, right)
    for key in repaired:
        candidates = [entry for entry in [left_data.get(key), right_data.get(key)] if entry is not None]
        winner = max(
            candidates,
            key=lambda entry: (int(entry["version"]), str(entry["value"])),
        )
        repaired_value = {
            "value": winner["value"],
            "version": int(winner["version"]),
        }
        left_data[key] = dict(repaired_value)
        right_data[key] = dict(repaired_value)
    return repaired


def visible_values(replica: dict[str, object]) -> dict[str, object]:
    data = replica["data"]
    assert isinstance(data, dict)
    return {
        key: entry["value"]
        for key, entry in data.items()
    }

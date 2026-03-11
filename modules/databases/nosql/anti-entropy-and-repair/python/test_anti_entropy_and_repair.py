from anti_entropy_and_repair import (
    divergent_keys,
    empty_replica,
    repair_pair,
    visible_values,
    write_value,
)


def test_divergent_keys_identifies_missing_and_stale_values():
    left = empty_replica("left")
    right = empty_replica("right")
    write_value(left, "doc:1", "v2", version=2)
    write_value(right, "doc:1", "v1", version=1)
    write_value(left, "doc:2", "left-only", version=1)

    assert divergent_keys(left, right) == ["doc:1", "doc:2"]


def test_repair_converges_both_replicas_to_latest_visible_values():
    left = empty_replica("left")
    right = empty_replica("right")
    write_value(left, "doc:1", "v2", version=2)
    write_value(right, "doc:1", "v1", version=1)
    write_value(right, "doc:2", "right-only", version=3)

    assert repair_pair(left, right) == ["doc:1", "doc:2"]
    assert visible_values(left) == {"doc:1": "v2", "doc:2": "right-only"}
    assert visible_values(right) == {"doc:1": "v2", "doc:2": "right-only"}

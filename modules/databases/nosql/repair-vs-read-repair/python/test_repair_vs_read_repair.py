from repair_vs_read_repair import (
    background_repair,
    divergent_keys,
    empty_replica,
    read_with_repair,
    visible_values,
    write_value,
)


def test_read_repair_only_fixes_the_key_that_was_read():
    left = empty_replica("left")
    right = empty_replica("right")
    write_value(left, "doc:1", "v2", version=2)
    write_value(right, "doc:1", "v1", version=1)
    write_value(left, "doc:2", "left-only", version=1)

    value, repaired = read_with_repair(left, right, "doc:1")

    assert value == "v2"
    assert repaired is True
    assert divergent_keys(left, right) == ["doc:2"]


def test_background_repair_converges_all_remaining_divergent_keys():
    left = empty_replica("left")
    right = empty_replica("right")
    write_value(left, "doc:1", "v2", version=2)
    write_value(right, "doc:1", "v1", version=1)
    write_value(right, "doc:2", "right-only", version=3)

    assert background_repair(left, right) == ["doc:1", "doc:2"]
    assert visible_values(left) == {"doc:1": "v2", "doc:2": "right-only"}
    assert visible_values(right) == {"doc:1": "v2", "doc:2": "right-only"}

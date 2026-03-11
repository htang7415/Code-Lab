from consumer_groups_and_offsets import assign_partitions, commit_offsets, poll_group


STREAM = {
    0: [
        {"partition": 0, "offset": 0, "value": "p0-a"},
        {"partition": 0, "offset": 1, "value": "p0-b"},
    ],
    1: [
        {"partition": 1, "offset": 0, "value": "p1-a"},
    ],
    2: [
        {"partition": 2, "offset": 0, "value": "p2-a"},
    ],
}


def test_round_robin_assignment_spreads_partitions_across_consumers() -> None:
    assert assign_partitions([0, 1, 2], ["c1", "c2"]) == {
        "c1": [0, 2],
        "c2": [1],
    }


def test_poll_reads_only_assigned_partitions_from_committed_offsets() -> None:
    assignments = assign_partitions([0, 1, 2], ["c1", "c2"])
    committed_offsets = {0: 1, 1: 0, 2: 0}

    assert poll_group(STREAM, assignments, committed_offsets, "c1") == [
        {"partition": 0, "offset": 1, "value": "p0-b"},
        {"partition": 2, "offset": 0, "value": "p2-a"},
    ]


def test_commit_offsets_advances_the_next_read_position_per_partition() -> None:
    committed_offsets = {0: 0, 2: 0}
    events = [
        {"partition": 0, "offset": 1, "value": "p0-b"},
        {"partition": 2, "offset": 0, "value": "p2-a"},
    ]

    commit_offsets(committed_offsets, events)

    assert committed_offsets == {0: 2, 2: 1}

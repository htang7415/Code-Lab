from write_skew_anomaly import (
    clinician,
    simulate_serial_schedule,
    simulate_write_skew,
)


def test_concurrent_snapshots_can_break_the_minimum_on_call_rule() -> None:
    initial = [
        clinician("alice", True),
        clinician("bob", True),
    ]

    summary = simulate_write_skew(
        initial_rows=initial,
        minimum_on_call=1,
        first_clinician="alice",
        second_clinician="bob",
    )

    assert summary == {
        "first_commits": True,
        "second_commits": True,
        "final_on_call_count": 0,
        "invariant_holds": False,
    }


def test_serial_execution_blocks_the_second_leave() -> None:
    initial = [
        clinician("alice", True),
        clinician("bob", True),
    ]

    summary = simulate_serial_schedule(
        initial_rows=initial,
        minimum_on_call=1,
        clinicians=["alice", "bob"],
    )

    assert summary == {
        "committed": ["alice"],
        "final_on_call_count": 1,
        "invariant_holds": True,
    }

"""write_skew_anomaly - concurrent snapshots can each preserve a local rule yet break a global invariant."""

from __future__ import annotations


def clinician(name: str, on_call: bool) -> dict[str, object]:
    return {
        "name": name,
        "on_call": on_call,
    }


def on_call_count(rows: list[dict[str, object]]) -> int:
    return sum(1 for row in rows if bool(row["on_call"]))


def can_leave_on_call(snapshot_rows: list[dict[str, object]], minimum_on_call: int) -> bool:
    return on_call_count(snapshot_rows) > minimum_on_call


def apply_leave_on_call(
    rows: list[dict[str, object]],
    clinician_name: str,
) -> list[dict[str, object]]:
    updated: list[dict[str, object]] = []
    for row in rows:
        next_row = dict(row)
        if str(row["name"]) == clinician_name:
            next_row["on_call"] = False
        updated.append(next_row)
    return updated


def simulate_write_skew(
    initial_rows: list[dict[str, object]],
    minimum_on_call: int,
    first_clinician: str,
    second_clinician: str,
) -> dict[str, object]:
    first_snapshot = [dict(row) for row in initial_rows]
    second_snapshot = [dict(row) for row in initial_rows]

    first_commits = can_leave_on_call(first_snapshot, minimum_on_call)
    second_commits = can_leave_on_call(second_snapshot, minimum_on_call)

    final_rows = [dict(row) for row in initial_rows]
    if first_commits:
        final_rows = apply_leave_on_call(final_rows, first_clinician)
    if second_commits:
        final_rows = apply_leave_on_call(final_rows, second_clinician)

    final_count = on_call_count(final_rows)
    return {
        "first_commits": first_commits,
        "second_commits": second_commits,
        "final_on_call_count": final_count,
        "invariant_holds": final_count >= minimum_on_call,
    }


def simulate_serial_schedule(
    initial_rows: list[dict[str, object]],
    minimum_on_call: int,
    clinicians: list[str],
) -> dict[str, object]:
    current_rows = [dict(row) for row in initial_rows]
    committed: list[str] = []
    for clinician_name in clinicians:
        if can_leave_on_call(current_rows, minimum_on_call):
            current_rows = apply_leave_on_call(current_rows, clinician_name)
            committed.append(clinician_name)

    final_count = on_call_count(current_rows)
    return {
        "committed": committed,
        "final_on_call_count": final_count,
        "invariant_holds": final_count >= minimum_on_call,
    }

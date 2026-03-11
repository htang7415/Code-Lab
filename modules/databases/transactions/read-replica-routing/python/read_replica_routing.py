"""read_replica_routing - route reads by comparing required and applied LSNs."""

from __future__ import annotations


def new_session_state() -> dict[str, int]:
    return {"required_lsn": 0}


def note_primary_write(session_state: dict[str, int], committed_lsn: int) -> None:
    session_state["required_lsn"] = max(
        int(session_state.get("required_lsn", 0)),
        committed_lsn,
    )


def replica_can_serve(
    session_state: dict[str, int],
    replica_applied_lsn: int,
) -> bool:
    return replica_applied_lsn >= int(session_state.get("required_lsn", 0))


def choose_read_target(
    session_state: dict[str, int],
    replica_applied_lsn: int,
    prefer_replica: bool = True,
) -> str:
    if prefer_replica and replica_can_serve(session_state, replica_applied_lsn):
        return "replica"
    return "primary"


def release_if_caught_up(
    session_state: dict[str, int],
    replica_applied_lsn: int,
) -> None:
    if replica_can_serve(session_state, replica_applied_lsn):
        session_state["required_lsn"] = 0

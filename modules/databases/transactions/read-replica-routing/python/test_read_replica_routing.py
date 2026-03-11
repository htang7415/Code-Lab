from read_replica_routing import (
    choose_read_target,
    new_session_state,
    note_primary_write,
    release_if_caught_up,
    replica_can_serve,
)


def test_session_routes_to_primary_until_replica_catches_up():
    session = new_session_state()
    note_primary_write(session, committed_lsn=10)

    assert not replica_can_serve(session, replica_applied_lsn=8)
    assert choose_read_target(session, replica_applied_lsn=8) == "primary"

    release_if_caught_up(session, replica_applied_lsn=10)

    assert choose_read_target(session, replica_applied_lsn=10) == "replica"


def test_read_only_session_can_use_replica_immediately():
    session = new_session_state()

    assert choose_read_target(session, replica_applied_lsn=0) == "replica"
    assert choose_read_target(session, replica_applied_lsn=0, prefer_replica=False) == "primary"

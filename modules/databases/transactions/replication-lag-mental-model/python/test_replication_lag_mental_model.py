from replication_lag_mental_model import (
    apply_replica_writes,
    commit_write,
    empty_primary_log,
    empty_replica_state,
    replica_lag,
    visible_value_on_primary,
    visible_value_on_replica,
)


def test_primary_commit_is_visible_before_replica_replay():
    primary_log = empty_primary_log()
    replica = empty_replica_state()

    lsn = commit_write(primary_log, "order:o1", {"status": "placed"})

    assert visible_value_on_primary(primary_log, "order:o1") == {"status": "placed"}
    assert visible_value_on_replica(replica, "order:o1") is None
    assert replica_lag(primary_log, replica) == 1

    assert apply_replica_writes(replica, primary_log, up_to_lsn=lsn) == [1]
    assert visible_value_on_replica(replica, "order:o1") == {"status": "placed"}
    assert replica_lag(primary_log, replica) == 0


def test_replica_can_be_behind_multiple_writes_and_deletes():
    primary_log = empty_primary_log()
    replica = empty_replica_state()

    first = commit_write(primary_log, "doc:1", {"status": "draft"})
    second = commit_write(primary_log, "doc:1", {"status": "published"})
    third = commit_write(primary_log, "doc:1", None)

    assert apply_replica_writes(replica, primary_log, up_to_lsn=second) == [1, 2]
    assert visible_value_on_replica(replica, "doc:1") == {"status": "published"}
    assert replica_lag(primary_log, replica) == 1

    assert apply_replica_writes(replica, primary_log, up_to_lsn=third) == [3]
    assert visible_value_on_replica(replica, "doc:1") is None

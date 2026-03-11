import pytest

from replica_failover_routing import (
    cluster_state,
    mark_node_down,
    mark_node_up,
    promote_replica,
    read_target,
    write_target,
)


def test_failover_promotes_healthy_replica_to_new_write_target():
    state = cluster_state("db-a", ["db-b", "db-c"])

    mark_node_down(state, "db-a")
    assert write_target(state) is None

    promote_replica(state, "db-b")

    assert write_target(state) == "db-b"
    assert read_target(state) == "db-c"


def test_unhealthy_replica_cannot_be_promoted():
    state = cluster_state("db-a", ["db-b"])
    mark_node_down(state, "db-b")

    with pytest.raises(ValueError):
        promote_replica(state, "db-b")

    mark_node_up(state, "db-b")
    promote_replica(state, "db-b")
    assert write_target(state) == "db-b"

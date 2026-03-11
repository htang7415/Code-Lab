"""replica_failover_routing - fail over writes to a promoted healthy replica."""

from __future__ import annotations


def cluster_state(primary: str, replicas: list[str]) -> dict[str, object]:
    healthy = {primary, *replicas}
    return {
        "primary": primary,
        "replicas": list(replicas),
        "healthy": healthy,
    }


def mark_node_down(state: dict[str, object], node_id: str) -> None:
    healthy = state["healthy"]
    assert isinstance(healthy, set)
    healthy.discard(node_id)


def mark_node_up(state: dict[str, object], node_id: str) -> None:
    healthy = state["healthy"]
    assert isinstance(healthy, set)
    healthy.add(node_id)


def promote_replica(state: dict[str, object], replica_id: str) -> None:
    replicas = state["replicas"]
    healthy = state["healthy"]
    assert isinstance(replicas, list)
    assert isinstance(healthy, set)
    if replica_id not in replicas:
        raise KeyError(replica_id)
    if replica_id not in healthy:
        raise ValueError("cannot promote unhealthy replica")

    previous_primary = str(state["primary"])
    replicas.remove(replica_id)
    if previous_primary != replica_id:
        replicas.append(previous_primary)
    state["primary"] = replica_id


def write_target(state: dict[str, object]) -> str | None:
    primary = str(state["primary"])
    healthy = state["healthy"]
    assert isinstance(healthy, set)
    return primary if primary in healthy else None


def read_target(state: dict[str, object], prefer_replica: bool = True) -> str | None:
    replicas = state["replicas"]
    healthy = state["healthy"]
    assert isinstance(replicas, list)
    assert isinstance(healthy, set)

    if prefer_replica:
        for replica_id in replicas:
            if replica_id in healthy:
                return replica_id
    return write_target(state)

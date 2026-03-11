from __future__ import annotations

import pytest

from consistency_tradeoffs import consistency_decision, consistency_mode, read_write_conflict_risk


def test_consistency_mode_depends_on_invariants_and_stale_read_tolerance() -> None:
    assert consistency_mode(cross_entity_invariant=True, stale_reads_tolerable=False) == "strong"
    assert consistency_mode(cross_entity_invariant=False, stale_reads_tolerable=True) == "eventual"
    assert consistency_mode(cross_entity_invariant=False, stale_reads_tolerable=False) == "session"


def test_read_write_conflict_risk_rises_with_more_writers_and_stricter_reads() -> None:
    assert read_write_conflict_risk(concurrent_writers=1, stale_reads_tolerable=False) == "low"
    assert read_write_conflict_risk(concurrent_writers=4, stale_reads_tolerable=True) == "medium"
    assert read_write_conflict_risk(concurrent_writers=4, stale_reads_tolerable=False) == "high"


def test_consistency_decision_maps_mode_and_risk_to_guidance() -> None:
    assert consistency_decision(
        cross_entity_invariant=True,
        stale_reads_tolerable=False,
        concurrent_writers=4,
    ) == "protect invariants with strong coordination"
    assert consistency_decision(
        cross_entity_invariant=False,
        stale_reads_tolerable=True,
        concurrent_writers=1,
    ) == "accept async replication and repair"

    with pytest.raises(ValueError):
        read_write_conflict_risk(concurrent_writers=-1, stale_reads_tolerable=False)

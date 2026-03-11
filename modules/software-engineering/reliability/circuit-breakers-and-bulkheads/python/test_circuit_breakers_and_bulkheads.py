from __future__ import annotations

import pytest

from circuit_breakers_and_bulkheads import allow_dependency_call, bulkhead_available, circuit_state


def test_circuit_state_transitions_from_closed_to_open_to_half_open() -> None:
    assert circuit_state(consecutive_failures=1, failure_threshold=4, cooldown_complete=False) == "closed"
    assert circuit_state(consecutive_failures=5, failure_threshold=4, cooldown_complete=False) == "open"
    assert circuit_state(consecutive_failures=5, failure_threshold=4, cooldown_complete=True) == "half-open"


def test_allow_dependency_call_uses_state_and_probe_budget() -> None:
    assert allow_dependency_call("closed") is True
    assert allow_dependency_call("open") is False
    assert allow_dependency_call("half-open", probe_budget=1) is True
    assert allow_dependency_call("half-open", probe_budget=0) is False


def test_bulkhead_available_blocks_when_capacity_is_exhausted() -> None:
    assert bulkhead_available(active_work=5, capacity=6) is True
    assert bulkhead_available(active_work=6, capacity=6) is False

    with pytest.raises(ValueError):
        bulkhead_available(active_work=-1, capacity=6)

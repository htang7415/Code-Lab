from __future__ import annotations

import pytest

from profiling_python import hotspot, profiling_next_step, python_bottleneck


def test_python_bottleneck_distinguishes_cpu_allocation_and_serialization_costs() -> None:
    assert python_bottleneck(cpu_ms=80, alloc_mb=20, serialization_ms=10) == "cpu"
    assert python_bottleneck(cpu_ms=20, alloc_mb=40, serialization_ms=10) == "allocation"
    assert python_bottleneck(cpu_ms=20, alloc_mb=10, serialization_ms=45) == "serialization"


def test_hotspot_returns_highest_cost_target() -> None:
    assert hotspot({"render": 12.0, "serialize": 45.0, "query_db": 20.0}) == "serialize"


def test_profiling_next_step_matches_python_bottleneck() -> None:
    assert profiling_next_step("cpu") == "inspect pure-python loops and algorithmic cost"
    assert profiling_next_step("serialization") == "inspect encoding, decoding, and schema conversion"

    with pytest.raises(ValueError):
        profiling_next_step("network")

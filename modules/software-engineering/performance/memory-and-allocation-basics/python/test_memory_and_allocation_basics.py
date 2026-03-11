from __future__ import annotations

import pytest

from memory_and_allocation_basics import allocation_bytes, memory_pressure, reuse_worth_it


def test_allocation_bytes_computes_total_allocation_volume() -> None:
    assert allocation_bytes(objects_per_request=500, bytes_per_object=256) == 128000


def test_memory_pressure_uses_heap_fraction_of_limit() -> None:
    assert memory_pressure(heap_mb=600, limit_mb=1024) == "low"
    assert memory_pressure(heap_mb=800, limit_mb=1024) == "medium"
    assert memory_pressure(heap_mb=950, limit_mb=1024) == "high"


def test_reuse_worth_it_flags_large_allocation_churn() -> None:
    assert reuse_worth_it(objects_per_request=5000, bytes_per_object=512) is True
    assert reuse_worth_it(objects_per_request=100, bytes_per_object=128) is False

    with pytest.raises(ValueError):
        allocation_bytes(objects_per_request=-1, bytes_per_object=10)

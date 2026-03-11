from __future__ import annotations

import pytest

from profiling_workflow import bottleneck_type, highest_cost_function, next_profiling_step


def test_bottleneck_type_chooses_dominant_cost_class() -> None:
    assert bottleneck_type(cpu_pct=75, io_wait_pct=10, alloc_pct=15) == "cpu"
    assert bottleneck_type(cpu_pct=20, io_wait_pct=50, alloc_pct=30) == "io"
    assert bottleneck_type(cpu_pct=20, io_wait_pct=10, alloc_pct=60) == "allocation"


def test_highest_cost_function_finds_main_profile_target() -> None:
    assert highest_cost_function({"render": 12.0, "query_db": 80.0, "serialize": 8.0}) == "query_db"


def test_next_profiling_step_depends_on_bottleneck_class() -> None:
    assert next_profiling_step("cpu") == "inspect hot functions and algorithm cost"
    assert next_profiling_step("allocation") == "inspect object churn and memory copies"

    with pytest.raises(ValueError):
        next_profiling_step("network")

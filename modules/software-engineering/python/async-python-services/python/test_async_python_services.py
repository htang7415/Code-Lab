from __future__ import annotations

import pytest

from async_python_services import async_service_fit, backpressure_needed, concurrency_budget


def test_async_service_fit_prefers_io_bound_workloads() -> None:
    assert async_service_fit(network_wait_ms=120, cpu_ms=20) is True
    assert async_service_fit(network_wait_ms=20, cpu_ms=120) is False


def test_concurrency_budget_scales_with_workers_and_in_flight_limit() -> None:
    assert concurrency_budget(worker_count=4, per_worker_in_flight=25) == 100


def test_backpressure_needed_when_in_flight_work_exceeds_budget() -> None:
    assert backpressure_needed(in_flight=120, budget=100) is True
    assert backpressure_needed(in_flight=80, budget=100) is False

    with pytest.raises(ValueError):
        concurrency_budget(worker_count=-1, per_worker_in_flight=10)

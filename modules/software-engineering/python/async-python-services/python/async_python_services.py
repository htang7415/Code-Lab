from __future__ import annotations


def async_service_fit(network_wait_ms: int, cpu_ms: int) -> bool:
    if network_wait_ms < 0 or cpu_ms < 0:
        raise ValueError("latencies must be non-negative")
    return network_wait_ms > cpu_ms


def concurrency_budget(worker_count: int, per_worker_in_flight: int) -> int:
    if worker_count < 0 or per_worker_in_flight < 0:
        raise ValueError("counts must be non-negative")
    return worker_count * per_worker_in_flight


def backpressure_needed(in_flight: int, budget: int) -> bool:
    if in_flight < 0 or budget < 0:
        raise ValueError("counts must be non-negative")
    return in_flight > budget

from __future__ import annotations


def bottleneck_type(cpu_pct: float, io_wait_pct: float, alloc_pct: float) -> str:
    if min(cpu_pct, io_wait_pct, alloc_pct) < 0:
        raise ValueError("percentages must be non-negative")
    if cpu_pct >= io_wait_pct and cpu_pct >= alloc_pct:
        return "cpu"
    if io_wait_pct >= cpu_pct and io_wait_pct >= alloc_pct:
        return "io"
    return "allocation"


def highest_cost_function(profile_costs_ms: dict[str, float]) -> str:
    if not profile_costs_ms:
        raise ValueError("profile_costs_ms must be non-empty")
    if any(cost < 0 for cost in profile_costs_ms.values()):
        raise ValueError("profile costs must be non-negative")
    return max(profile_costs_ms, key=profile_costs_ms.get)


def next_profiling_step(bottleneck: str) -> str:
    normalized = bottleneck.strip().lower()
    if normalized == "cpu":
        return "inspect hot functions and algorithm cost"
    if normalized == "io":
        return "inspect external calls and wait time"
    if normalized == "allocation":
        return "inspect object churn and memory copies"
    raise ValueError("bottleneck must be cpu, io, or allocation")

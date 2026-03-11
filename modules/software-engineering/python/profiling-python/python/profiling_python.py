from __future__ import annotations


def python_bottleneck(cpu_ms: float, alloc_mb: float, serialization_ms: float) -> str:
    if min(cpu_ms, alloc_mb, serialization_ms) < 0:
        raise ValueError("costs must be non-negative")
    if cpu_ms >= alloc_mb and cpu_ms >= serialization_ms:
        return "cpu"
    if alloc_mb >= cpu_ms and alloc_mb >= serialization_ms:
        return "allocation"
    return "serialization"


def hotspot(costs: dict[str, float]) -> str:
    if not costs:
        raise ValueError("costs must be non-empty")
    if any(cost < 0 for cost in costs.values()):
        raise ValueError("costs must be non-negative")
    return max(costs, key=costs.get)


def profiling_next_step(bottleneck: str) -> str:
    normalized = bottleneck.strip().lower()
    if normalized == "cpu":
        return "inspect pure-python loops and algorithmic cost"
    if normalized == "allocation":
        return "inspect object churn and temporary allocations"
    if normalized == "serialization":
        return "inspect encoding, decoding, and schema conversion"
    raise ValueError("unknown bottleneck")

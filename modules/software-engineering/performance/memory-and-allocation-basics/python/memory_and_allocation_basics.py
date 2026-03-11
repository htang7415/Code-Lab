from __future__ import annotations


def allocation_bytes(objects_per_request: int, bytes_per_object: int) -> int:
    if objects_per_request < 0 or bytes_per_object < 0:
        raise ValueError("counts and sizes must be non-negative")
    return objects_per_request * bytes_per_object


def memory_pressure(heap_mb: int, limit_mb: int) -> str:
    if heap_mb < 0 or limit_mb <= 0:
        raise ValueError("heap_mb must be non-negative and limit_mb positive")
    usage = heap_mb / limit_mb
    if usage >= 0.9:
        return "high"
    if usage >= 0.7:
        return "medium"
    return "low"


def reuse_worth_it(objects_per_request: int, bytes_per_object: int) -> bool:
    return allocation_bytes(objects_per_request, bytes_per_object) >= 1_000_000

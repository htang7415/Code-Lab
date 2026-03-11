from __future__ import annotations


def preferred_delivery_mode(needs_early_results: bool, amortization_priority: bool) -> str:
    if needs_early_results:
        return "streaming"
    if amortization_priority:
        return "batching"
    return "batching"


def batch_cost_per_item(total_batch_ms: int, batch_size: int) -> float:
    if total_batch_ms < 0 or batch_size <= 0:
        raise ValueError("total_batch_ms must be non-negative and batch_size positive")
    return total_batch_ms / batch_size


def streaming_worth_it(time_to_first_result_ms: int, full_completion_ms: int) -> bool:
    if time_to_first_result_ms < 0 or full_completion_ms < 0:
        raise ValueError("latencies must be non-negative")
    if full_completion_ms == 0:
        return False
    return time_to_first_result_ms <= full_completion_ms / 4

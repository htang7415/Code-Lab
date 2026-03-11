from __future__ import annotations


def remaining_latency_budget(
    total_budget_ms: int,
    elapsed_ms: int,
    reserved_response_ms: int = 0,
) -> int:
    if total_budget_ms <= 0:
        raise ValueError("total_budget_ms must be positive")
    if elapsed_ms < 0:
        raise ValueError("elapsed_ms must be non-negative")
    if reserved_response_ms < 0:
        raise ValueError("reserved_response_ms must be non-negative")
    if reserved_response_ms >= total_budget_ms:
        raise ValueError("reserved_response_ms must be smaller than total_budget_ms")

    return max(total_budget_ms - reserved_response_ms - elapsed_ms, 0)


def per_step_latency_budget(remaining_budget_ms: int, remaining_steps: int) -> int:
    if remaining_budget_ms < 0:
        raise ValueError("remaining_budget_ms must be non-negative")
    if remaining_steps <= 0:
        raise ValueError("remaining_steps must be positive")
    return remaining_budget_ms // remaining_steps


def latency_budget_route(
    step_latency_ms: int,
    step_budget_ms: int,
    can_stream: bool,
    can_fallback: bool,
) -> str:
    if step_latency_ms < 0:
        raise ValueError("step_latency_ms must be non-negative")
    if step_budget_ms <= 0:
        raise ValueError("step_budget_ms must be positive")

    if step_latency_ms <= step_budget_ms:
        return "continue"
    if can_stream:
        return "stream"
    if can_fallback:
        return "fallback"
    return "review"

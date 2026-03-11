from __future__ import annotations


def should_background_job(user_waiting: bool, duration_ms: int, retries_expected: bool) -> bool:
    if duration_ms < 0:
        raise ValueError("duration_ms must be non-negative")
    return duration_ms >= 500 or retries_expected or not user_waiting


def workflow_kind(needs_human_approval: bool, has_multiple_steps: bool) -> str:
    if needs_human_approval or has_multiple_steps:
        return "workflow"
    return "single-job"


def queue_priority(user_visible: bool, deadline_ms: int | None) -> str:
    if deadline_ms is not None and deadline_ms < 0:
        raise ValueError("deadline_ms must be non-negative when provided")
    if user_visible and deadline_ms is not None and deadline_ms <= 5000:
        return "high"
    if user_visible:
        return "medium"
    return "low"

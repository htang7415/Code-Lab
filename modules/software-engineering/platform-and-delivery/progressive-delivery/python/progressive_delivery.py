from __future__ import annotations


ROLLOUT_STEPS = [1, 5, 10, 25, 50, 100]


def next_rollout_stage(current_percentage: int, healthy: bool) -> int:
    if current_percentage not in ROLLOUT_STEPS:
        raise ValueError("current_percentage must be one of the rollout steps")
    if not healthy:
        return current_percentage
    index = ROLLOUT_STEPS.index(current_percentage)
    return ROLLOUT_STEPS[min(index + 1, len(ROLLOUT_STEPS) - 1)]


def blast_radius(current_percentage: int, total_users: int) -> int:
    if total_users < 0:
        raise ValueError("total_users must be non-negative")
    return (current_percentage * total_users) // 100


def should_pause_rollout(error_rate_delta: float, max_allowed_delta: float) -> bool:
    if error_rate_delta < 0 or max_allowed_delta < 0:
        raise ValueError("deltas must be non-negative")
    return error_rate_delta > max_allowed_delta

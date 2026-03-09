from __future__ import annotations

import math


def _event_rate(event_count: int, total_count: int) -> float:
    if total_count < 0:
        raise ValueError("total_count must be non-negative")
    if event_count < 0:
        raise ValueError("event_count must be non-negative")
    if event_count > total_count:
        raise ValueError("event_count cannot exceed total_count")
    if total_count == 0:
        return 0.0
    return event_count / total_count


def log_rate_ratio(
    event_count: int,
    total_count: int,
    baseline_event_count: int,
    baseline_total_count: int,
) -> float:
    rate = _event_rate(event_count, total_count)
    baseline_rate = _event_rate(baseline_event_count, baseline_total_count)
    if rate == 0.0 and baseline_rate == 0.0:
        return 0.0
    if baseline_rate == 0.0:
        return float("inf")
    if rate == 0.0:
        return float("-inf")
    return math.log(rate / baseline_rate)

from __future__ import annotations

import math


def _validate_binary_labels(labels: list[int]) -> None:
    if any(label not in {0, 1} for label in labels):
        raise ValueError("labels must contain only 0 or 1")


def positive_rate(labels: list[int]) -> float:
    _validate_binary_labels(labels)
    if not labels:
        return 0.0
    return sum(labels) / len(labels)


def base_rate_gap(group_a: list[int], group_b: list[int]) -> float:
    return positive_rate(group_a) - positive_rate(group_b)


def prevalence_delta(baseline_labels: list[int], comparison_labels: list[int]) -> float:
    return positive_rate(comparison_labels) - positive_rate(baseline_labels)


def prevalence_ratio(group_a: list[int], group_b: list[int]) -> float:
    rate_a = positive_rate(group_a)
    rate_b = positive_rate(group_b)
    if rate_b == 0.0:
        return 0.0 if rate_a == 0.0 else float("inf")
    return rate_a / rate_b


def risk_ratio(exposed_labels: list[int], baseline_labels: list[int]) -> float:
    return prevalence_ratio(exposed_labels, baseline_labels)


def base_rate_ratio(group_a: list[int], group_b: list[int]) -> float:
    return prevalence_ratio(group_a, group_b)


def prevalence_index(labels: list[int], baseline_rate: float) -> float:
    if not 0.0 <= baseline_rate <= 1.0:
        raise ValueError("baseline_rate must lie in [0, 1]")

    rate = positive_rate(labels)
    if baseline_rate == 0.0:
        return 0.0 if rate == 0.0 else float("inf")
    return rate / baseline_rate


def prevalence_odds(labels: list[int]) -> float:
    rate = positive_rate(labels)
    if rate == 1.0:
        return float("inf")
    return rate / (1.0 - rate)


def log_prevalence_ratio(group_a: list[int], group_b: list[int]) -> float:
    rate_a = positive_rate(group_a)
    rate_b = positive_rate(group_b)
    if rate_a == 0.0 and rate_b == 0.0:
        return 0.0
    if rate_b == 0.0:
        return float("inf")
    if rate_a == 0.0:
        return float("-inf")
    return math.log(rate_a / rate_b)


def log_risk_ratio(exposed_labels: list[int], baseline_labels: list[int]) -> float:
    return log_prevalence_ratio(exposed_labels, baseline_labels)


def log_relative_risk(exposed_labels: list[int], baseline_labels: list[int]) -> float:
    return log_prevalence_ratio(exposed_labels, baseline_labels)


def log_odds(labels: list[int]) -> float:
    rate = positive_rate(labels)
    if rate == 0.0:
        return float("-inf")
    if rate == 1.0:
        return float("inf")
    return math.log(rate / (1.0 - rate))


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

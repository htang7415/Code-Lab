from __future__ import annotations


def platform_candidate(teams: int, repeated_work_hours_per_team: int, custom_exceptions: int) -> bool:
    if teams < 0 or repeated_work_hours_per_team < 0 or custom_exceptions < 0:
        raise ValueError("inputs must be non-negative")
    return teams >= 3 and repeated_work_hours_per_team >= 2 and custom_exceptions <= 3


def abstraction_risk(custom_exceptions: int) -> str:
    if custom_exceptions < 0:
        raise ValueError("custom_exceptions must be non-negative")
    if custom_exceptions <= 1:
        return "low"
    if custom_exceptions <= 3:
        return "medium"
    return "high"


def platform_value(teams: int, repeated_work_hours_per_team: int) -> int:
    if teams < 0 or repeated_work_hours_per_team < 0:
        raise ValueError("inputs must be non-negative")
    return teams * repeated_work_hours_per_team

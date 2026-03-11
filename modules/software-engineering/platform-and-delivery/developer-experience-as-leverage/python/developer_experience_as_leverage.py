from __future__ import annotations


def feedback_loop_risk(setup_minutes: int, test_minutes: int, deploy_feedback_minutes: int) -> str:
    if min(setup_minutes, test_minutes, deploy_feedback_minutes) < 0:
        raise ValueError("times must be non-negative")
    total = setup_minutes + test_minutes + deploy_feedback_minutes
    if total >= 30:
        return "high"
    if total >= 10:
        return "medium"
    return "low"


def dx_investment_worth_it(engineers: int, minutes_saved_per_week: int) -> bool:
    if engineers < 0 or minutes_saved_per_week < 0:
        raise ValueError("inputs must be non-negative")
    return engineers * minutes_saved_per_week >= 120


def dx_priority(setup_minutes: int, test_minutes: int, deploy_feedback_minutes: int) -> str:
    if min(setup_minutes, test_minutes, deploy_feedback_minutes) < 0:
        raise ValueError("times must be non-negative")
    costs = {
        "setup": setup_minutes,
        "test-feedback": test_minutes,
        "deploy-feedback": deploy_feedback_minutes,
    }
    return max(costs, key=costs.get)

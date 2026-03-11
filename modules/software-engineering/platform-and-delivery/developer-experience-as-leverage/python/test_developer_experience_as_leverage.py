from __future__ import annotations

import pytest

from developer_experience_as_leverage import (
    dx_investment_worth_it,
    dx_priority,
    feedback_loop_risk,
)


def test_feedback_loop_risk_uses_total_delay_across_main_dev_loop_steps() -> None:
    assert feedback_loop_risk(setup_minutes=20, test_minutes=15, deploy_feedback_minutes=10) == "high"
    assert feedback_loop_risk(setup_minutes=5, test_minutes=3, deploy_feedback_minutes=2) == "medium"
    assert feedback_loop_risk(setup_minutes=1, test_minutes=1, deploy_feedback_minutes=1) == "low"


def test_dx_investment_worth_it_estimates_org_wide_time_saved() -> None:
    assert dx_investment_worth_it(engineers=10, minutes_saved_per_week=30) is True
    assert dx_investment_worth_it(engineers=2, minutes_saved_per_week=20) is False


def test_dx_priority_targets_the_worst_feedback_loop_cost() -> None:
    assert dx_priority(setup_minutes=20, test_minutes=5, deploy_feedback_minutes=8) == "setup"

    with pytest.raises(ValueError):
        dx_priority(setup_minutes=-1, test_minutes=5, deploy_feedback_minutes=8)

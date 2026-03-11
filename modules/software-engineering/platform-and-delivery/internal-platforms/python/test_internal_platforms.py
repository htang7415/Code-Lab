from __future__ import annotations

import pytest

from internal_platforms import abstraction_risk, platform_candidate, platform_value


def test_platform_candidate_requires_repeated_multi_team_pain_and_limited_exceptions() -> None:
    assert platform_candidate(teams=6, repeated_work_hours_per_team=5, custom_exceptions=1) is True
    assert platform_candidate(teams=2, repeated_work_hours_per_team=5, custom_exceptions=1) is False
    assert platform_candidate(teams=6, repeated_work_hours_per_team=5, custom_exceptions=5) is False


def test_abstraction_risk_rises_with_more_special_cases() -> None:
    assert abstraction_risk(custom_exceptions=1) == "low"
    assert abstraction_risk(custom_exceptions=3) == "medium"
    assert abstraction_risk(custom_exceptions=5) == "high"


def test_platform_value_estimates_repeated_hours_removed() -> None:
    assert platform_value(teams=6, repeated_work_hours_per_team=5) == 30

    with pytest.raises(ValueError):
        platform_value(teams=-1, repeated_work_hours_per_team=5)

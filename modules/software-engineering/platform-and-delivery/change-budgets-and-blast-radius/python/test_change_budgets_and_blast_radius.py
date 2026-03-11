from __future__ import annotations

import pytest

from change_budgets_and_blast_radius import (
    blast_radius,
    change_budget_available,
    progressive_delivery_required,
)


def test_blast_radius_combines_audience_state_and_region_risk() -> None:
    assert blast_radius(users_affected_percent=5, touches_write_path=False, multi_region=False) == "low"
    assert blast_radius(users_affected_percent=40, touches_write_path=False, multi_region=False) == "medium"
    assert blast_radius(users_affected_percent=40, touches_write_path=True, multi_region=False) == "high"


def test_change_budget_available_shrinks_under_parallel_risk_or_oncall_pressure() -> None:
    assert change_budget_available(open_high_risk_changes=0, oncall_load="low") is True
    assert change_budget_available(open_high_risk_changes=1, oncall_load="medium") is False
    assert change_budget_available(open_high_risk_changes=0, oncall_load="high") is False


def test_progressive_delivery_required_for_any_nontrivial_change() -> None:
    assert progressive_delivery_required("low", True) is False
    assert progressive_delivery_required("medium", True) is True
    assert progressive_delivery_required("low", False) is True

    with pytest.raises(ValueError):
        change_budget_available(open_high_risk_changes=0, oncall_load="urgent")

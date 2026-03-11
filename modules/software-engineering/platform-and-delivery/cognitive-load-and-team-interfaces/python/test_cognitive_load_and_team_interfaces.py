from __future__ import annotations

import pytest

from cognitive_load_and_team_interfaces import (
    boundary_rework_needed,
    interface_clarity,
    team_cognitive_load,
)


def test_team_cognitive_load_estimates_operational_burden() -> None:
    assert team_cognitive_load(services=1, workflows=1, pager_domains=1) == "low"
    assert team_cognitive_load(services=2, workflows=2, pager_domains=2) == "medium"
    assert team_cognitive_load(services=5, workflows=4, pager_domains=3) == "high"


def test_interface_clarity_detects_shared_ownership_pressure() -> None:
    assert interface_clarity(owned_components=4, shared_components=0) == "clear"
    assert interface_clarity(owned_components=4, shared_components=1) == "mixed"
    assert interface_clarity(owned_components=2, shared_components=2) == "blurred"


def test_boundary_rework_needed_flags_overloaded_or_blurry_boundaries() -> None:
    assert boundary_rework_needed("high", "clear") is True
    assert boundary_rework_needed("medium", "blurred") is True
    assert boundary_rework_needed("medium", "mixed") is False

    with pytest.raises(ValueError):
        team_cognitive_load(services=-1, workflows=1, pager_domains=1)

from __future__ import annotations

import pytest

from stateless_vs_stateful_design import component_style, horizontal_scaling_ease, recovery_complexity


def test_component_style_depends_on_persistent_or_locally_consistent_state() -> None:
    assert component_style(needs_durable_session=False, requires_local_cache_consistency=False) == "stateless"
    assert component_style(needs_durable_session=True, requires_local_cache_consistency=False) == "stateful"


def test_stateless_design_scales_and_recovers_more_easily() -> None:
    assert horizontal_scaling_ease("stateless") == "easy"
    assert recovery_complexity("stateless") == "lower"
    assert horizontal_scaling_ease("stateful") == "harder"
    assert recovery_complexity("stateful") == "higher"


def test_validation_rejects_unknown_styles() -> None:
    with pytest.raises(ValueError):
        horizontal_scaling_ease("hybrid")

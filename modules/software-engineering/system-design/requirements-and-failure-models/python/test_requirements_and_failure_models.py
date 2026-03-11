from __future__ import annotations

import pytest

from requirements_and_failure_models import (
    architecture_focus,
    dominant_failure_model,
    required_quality_attributes,
)


def test_required_quality_attributes_reflect_product_shape() -> None:
    assert required_quality_attributes(user_facing=True, high_scale=True, strict_correctness=False) == [
        "latency",
        "availability",
        "scalability",
    ]
    assert required_quality_attributes(user_facing=False, high_scale=False, strict_correctness=False) == [
        "simplicity"
    ]


def test_dominant_failure_model_prefers_overload_then_dependency_then_state() -> None:
    assert dominant_failure_model(external_dependencies=4, stateful_components=1, overload_risk=True) == "overload"
    assert dominant_failure_model(external_dependencies=4, stateful_components=1, overload_risk=False) == "dependency-failure"
    assert dominant_failure_model(external_dependencies=1, stateful_components=3, overload_risk=False) == "state-failure"


def test_architecture_focus_maps_failure_model_to_design_priority() -> None:
    assert architecture_focus(["latency"], "overload") == "shed load and protect tail latency"
    assert architecture_focus(["availability"], "dependency-failure") == "isolate dependencies and add fallbacks"

    with pytest.raises(ValueError):
        architecture_focus(["latency"], "unknown")

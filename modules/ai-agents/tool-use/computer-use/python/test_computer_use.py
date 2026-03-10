from __future__ import annotations

import pytest

from computer_use import action_requires_target, step_within_budget, ui_action


def test_computer_use_helpers_validate_targets_and_steps() -> None:
    assert action_requires_target("click") is True
    assert action_requires_target("wait") is False
    assert ui_action("click", target="Submit button") == {
        "action": "click",
        "target": "Submit button",
        "text": None,
    }
    assert step_within_budget(3, 10) is True


def test_type_actions_require_text() -> None:
    assert ui_action("type", target="Search box", text="weather")["text"] == "weather"
    with pytest.raises(ValueError):
        ui_action("type", target="Search box")


def test_computer_use_validation_rejects_missing_targets_or_bad_budgets() -> None:
    with pytest.raises(ValueError):
        ui_action("click")
    with pytest.raises(ValueError):
        step_within_budget(-1, 3)

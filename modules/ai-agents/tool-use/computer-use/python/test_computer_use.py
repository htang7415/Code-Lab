from __future__ import annotations

import pytest

from computer_use import (
    action_requires_checkpoint,
    action_requires_target,
    should_takeover,
    step_within_budget,
    ui_action,
    unsafe_screen_detected,
)


def test_computer_use_helpers_validate_targets_and_steps() -> None:
    assert action_requires_target("click") is True
    assert action_requires_target("wait") is False
    assert ui_action("click", target="Submit button") == {
        "action": "click",
        "target": "Submit button",
        "text": None,
    }
    assert step_within_budget(3, 10) is True
    assert action_requires_checkpoint("click", "Submit order") is True
    assert should_takeover(checkpoint_required=True, unsafe_screen=False) is True


def test_type_actions_require_text() -> None:
    assert ui_action("type", target="Search box", text="weather")["text"] == "weather"
    assert unsafe_screen_detected("Enter your password to continue") is True
    assert should_takeover(checkpoint_required=False, unsafe_screen=True) is True
    with pytest.raises(ValueError):
        ui_action("type", target="Search box")


def test_computer_use_validation_rejects_missing_targets_or_bad_budgets() -> None:
    with pytest.raises(ValueError):
        ui_action("click")
    with pytest.raises(ValueError):
        step_within_budget(-1, 3)
    with pytest.raises(ValueError):
        action_requires_checkpoint("")
    with pytest.raises(ValueError):
        unsafe_screen_detected(" ")

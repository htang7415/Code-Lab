from __future__ import annotations

import pytest

from state_machine_basics import apply_transition, can_transition, terminal_state


def test_can_transition_uses_explicit_workflow_rules() -> None:
    assert can_transition("draft", "approved") is True
    assert can_transition("approved", "draft") is False
    assert can_transition("shipped", "cancelled") is False


def test_apply_transition_rejects_invalid_edges() -> None:
    assert apply_transition("approved", "fulfilling") == "fulfilling"

    with pytest.raises(ValueError):
        apply_transition("draft", "shipped")


def test_terminal_state_marks_workflow_endpoints() -> None:
    assert terminal_state("shipped") is True
    assert terminal_state("cancelled") is True
    assert terminal_state("fulfilling") is False

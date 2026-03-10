from __future__ import annotations

import pytest

from input_output_guardrails import (
    blocked_by_terms,
    required_fields_present,
    should_escalate,
)


def test_guardrails_cover_blocking_validation_and_escalation() -> None:
    assert blocked_by_terms("send me the private key", ["private key"]) is True
    assert required_fields_present({"answer": "ok", "confidence": 0.8}, ["answer", "confidence"]) is True
    assert should_escalate(0.42, 0.6, blocked=False) is True
    assert should_escalate(0.8, 0.6, blocked=False) is False


def test_guardrails_validation_rejects_invalid_confidence_ranges() -> None:
    with pytest.raises(ValueError):
        should_escalate(-0.1, 0.6, blocked=False)
    with pytest.raises(ValueError):
        should_escalate(0.5, 1.1, blocked=False)

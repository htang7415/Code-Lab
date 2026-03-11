from __future__ import annotations

import pytest

from security_and_red_team_evals import (
    high_risk_failure_count,
    security_eval_breakdown,
    security_release_gate,
)


def test_security_and_red_team_evals_build_breakdown_and_count_high_risk() -> None:
    breakdown = security_eval_breakdown(
        ["prompt_injection", "unsafe_action", "prompt_injection"]
    )
    assert breakdown == {
        "prompt_injection": 2,
        "unsafe_action": 1,
    }
    assert high_risk_failure_count(breakdown) == 3


def test_security_release_gate_distinguishes_pass_review_and_fail() -> None:
    assert security_release_gate(pass_rate=0.95, high_risk_failures=0, min_pass_rate=0.9) == "pass"
    assert security_release_gate(pass_rate=0.84, high_risk_failures=0, min_pass_rate=0.9) == "review"
    assert security_release_gate(pass_rate=0.97, high_risk_failures=1, min_pass_rate=0.9) == "fail"


def test_security_and_red_team_evals_validation() -> None:
    with pytest.raises(ValueError):
        security_eval_breakdown([])
    with pytest.raises(ValueError):
        high_risk_failure_count({})
    with pytest.raises(ValueError):
        security_release_gate(pass_rate=1.1, high_risk_failures=0, min_pass_rate=0.9)
    with pytest.raises(ValueError):
        security_release_gate(pass_rate=0.9, high_risk_failures=-1, min_pass_rate=0.9)

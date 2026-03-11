from __future__ import annotations

import pytest

from evaluator_optimizer_loops import (
    evaluation_report,
    optimizer_route,
    revision_packet,
)


def test_evaluator_optimizer_loop_builds_report_and_revision_packet() -> None:
    report = evaluation_report({"citations": True, "clarity": False, "format": False})

    assert report == {
        "passed": False,
        "passed_checks": ["citations"],
        "failed_checks": ["clarity", "format"],
        "score": 1 / 3,
    }
    assert revision_packet("Draft answer", report["failed_checks"]) == {
        "draft": "Draft answer",
        "feedback": ["clarity", "format"],
    }


def test_evaluator_optimizer_route_distinguishes_accept_revise_and_escalate() -> None:
    assert optimizer_route(True, attempt=0, max_attempts=3) == "accept"
    assert optimizer_route(False, attempt=0, max_attempts=3) == "revise"
    assert optimizer_route(False, attempt=2, max_attempts=3) == "escalate"


def test_evaluator_optimizer_loop_validation() -> None:
    with pytest.raises(ValueError):
        evaluation_report({})
    with pytest.raises(ValueError):
        optimizer_route(False, attempt=-1, max_attempts=3)
    with pytest.raises(ValueError):
        revision_packet("", ["clarity"])
    with pytest.raises(ValueError):
        revision_packet("Draft", [])

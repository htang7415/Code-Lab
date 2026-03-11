from __future__ import annotations

from spec_first_ai_coding import (
    missing_spec_sections,
    review_focus,
    spec_ready_for_generation,
)


def test_missing_spec_sections_reports_unwritten_requirements() -> None:
    required = ["contract", "invariants", "tests", "rollback"]
    present = ["contract", "tests"]

    assert missing_spec_sections(required, present) == ["invariants", "rollback"]


def test_spec_ready_for_generation_requires_full_spec_shape() -> None:
    required = ["contract", "tests"]

    assert spec_ready_for_generation(required, ["contract", "tests"]) is True
    assert spec_ready_for_generation(required, ["contract"]) is False


def test_review_focus_expands_with_change_risk() -> None:
    assert review_focus(["api", "mutation", "ai-generated"]) == [
        "contract",
        "compatibility",
        "invariants",
        "regression",
    ]

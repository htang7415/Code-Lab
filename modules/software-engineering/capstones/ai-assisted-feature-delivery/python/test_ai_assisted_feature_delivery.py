from __future__ import annotations

from ai_assisted_feature_delivery import (
    delivery_decision,
    required_spec_sections,
    review_blockers,
    spec_gaps,
    verification_strength,
)


def test_required_spec_sections_expand_with_change_risk() -> None:
    assert required_spec_sections(["api", "security", "rollout"]) == [
        "contract",
        "invariants",
        "tests",
        "rollback",
        "compatibility",
        "security",
        "observability",
    ]


def test_spec_gaps_and_review_blockers_gate_generated_changes() -> None:
    assert spec_gaps(["api"], ["contract", "tests"]) == ["invariants", "rollback", "compatibility"]
    assert review_blockers(
        ["api", "ai-generated"],
        {"correctness": True, "tests": True, "compatibility": False, "regression": True},
    ) == ["compatibility"]


def test_delivery_decision_requires_spec_review_verification_and_rollback() -> None:
    tags = ["api", "ai-generated"]
    sections = ["contract", "invariants", "tests", "rollback", "compatibility"]
    review = {"correctness": True, "tests": True, "compatibility": True, "regression": True}

    assert verification_strength(True, True, True) == "strong"
    assert delivery_decision(tags, sections, review, True, True, True, True) == "ship-canary"
    assert delivery_decision(tags, sections, review, True, True, False, True) == "fix-verification"
    assert delivery_decision(tags, sections, review, True, True, True, False) == "hold"

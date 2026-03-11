from __future__ import annotations

from generated_code_review_checklists import (
    missing_review_items,
    review_checklist,
    review_complete,
)


def test_review_checklist_expands_with_change_risk() -> None:
    assert review_checklist(["api", "security", "ai-generated"]) == [
        "correctness",
        "tests",
        "compatibility",
        "security",
        "regression",
    ]


def test_missing_review_items_reports_incomplete_gates() -> None:
    required = review_checklist(["api"])
    completed = {"correctness": True, "tests": True, "compatibility": False}

    assert missing_review_items(required, completed) == ["compatibility"]


def test_review_complete_requires_all_items_to_be_done() -> None:
    required = review_checklist(["security"])

    assert review_complete(required, {"correctness": True, "tests": True, "security": True}) is True
    assert review_complete(required, {"correctness": True, "tests": True}) is False

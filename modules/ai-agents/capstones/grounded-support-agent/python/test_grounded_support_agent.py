from __future__ import annotations

from grounded_support_agent import build_support_context, grounded_support_decision


def test_build_support_context_keeps_top_chunks_and_recent_memory() -> None:
    context = build_support_context(
        [("policy doc", 0.6), ("billing faq", 0.9), ("old note", 0.2)],
        ["prefers csv", "needs invoice copy"],
        max_chunks=2,
        max_memories=1,
    )

    assert context == {
        "retrieved": ["billing faq", "policy doc"],
        "memories": ["needs invoice copy"],
        "context_blocks": ["billing faq", "policy doc", "needs invoice copy"],
    }


def test_grounded_support_decision_blocks_or_reviews_when_needed() -> None:
    blocked = grounded_support_decision(
        [("billing faq", 0.9)],
        ["prefers csv"],
        {"search": {"success_probability": 0.9, "success_value": 3.0, "tool_cost": 0.5}},
        blocked=True,
        confidence=0.9,
        grounding_coverage=0.9,
    )
    low_grounding = grounded_support_decision(
        [("billing faq", 0.9)],
        ["prefers csv"],
        {"search": {"success_probability": 0.9, "success_value": 3.0, "tool_cost": 0.5}},
        blocked=False,
        confidence=0.9,
        grounding_coverage=0.5,
    )

    assert blocked["route"] == "block"
    assert low_grounding["route"] == "review"


def test_grounded_support_decision_selects_strong_tool() -> None:
    decision = grounded_support_decision(
        [("billing faq", 0.9)],
        ["prefers csv"],
        {
            "ticket_lookup": {
                "success_probability": 0.9,
                "success_value": 5.0,
                "tool_cost": 0.5,
                "failure_penalty": 0.2,
            },
            "slow_export": {
                "success_probability": 0.6,
                "success_value": 2.0,
                "tool_cost": 1.0,
                "failure_penalty": 0.5,
            },
        },
        blocked=False,
        confidence=0.85,
        grounding_coverage=0.9,
        min_expected_value=2.0,
        min_margin=0.2,
    )

    assert decision["route"] == "tool:ticket_lookup"


def test_grounded_support_decision_answers_from_context_when_tool_is_not_worth_it() -> None:
    decision = grounded_support_decision(
        [("billing faq", 0.9)],
        ["prefers csv"],
        {
            "ticket_lookup": {
                "success_probability": 0.4,
                "success_value": 2.0,
                "tool_cost": 1.5,
                "failure_penalty": 0.5,
            }
        },
        blocked=False,
        confidence=0.88,
        grounding_coverage=0.92,
        min_expected_value=0.5,
    )

    assert decision["route"] == "answer-from-context"

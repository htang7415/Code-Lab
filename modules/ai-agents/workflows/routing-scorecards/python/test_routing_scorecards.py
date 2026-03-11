from __future__ import annotations

import pytest

from routing_scorecards import route_score, score_routes, scorecard_route


def test_routing_scorecards_score_and_rank_routes() -> None:
    weights = {
        "task_fit": 0.5,
        "tool_readiness": 0.3,
        "latency_fit": 0.2,
    }
    candidates = {
        "search-docs": {
            "task_fit": 0.92,
            "tool_readiness": 0.80,
            "latency_fit": 0.70,
        },
        "email-agent": {
            "task_fit": 0.40,
            "tool_readiness": 0.95,
            "latency_fit": 0.90,
        },
    }

    assert route_score(candidates["search-docs"], weights) == pytest.approx(0.84)
    assert score_routes(candidates, weights) == [
        {"route": "search-docs", "score": pytest.approx(0.84)},
        {"route": "email-agent", "score": pytest.approx(0.665)},
    ]
    assert scorecard_route(candidates, weights, min_score=0.75, min_margin=0.05) == "search-docs"


def test_routing_scorecards_review_weak_or_ambiguous_winners() -> None:
    weights = {"task_fit": 0.6, "tool_readiness": 0.4}

    assert (
        scorecard_route(
            {
                "route-a": {"task_fit": 0.62, "tool_readiness": 0.58},
                "route-b": {"task_fit": 0.55, "tool_readiness": 0.54},
            },
            weights,
            min_score=0.70,
        )
        == "review"
    )

    assert (
        scorecard_route(
            {
                "route-a": {"task_fit": 0.86, "tool_readiness": 0.74},
                "route-b": {"task_fit": 0.84, "tool_readiness": 0.75},
            },
            weights,
            min_score=0.70,
            min_margin=0.02,
        )
        == "review"
    )


def test_routing_scorecards_validation() -> None:
    with pytest.raises(ValueError):
        route_score({}, {"task_fit": 1.0})
    with pytest.raises(ValueError):
        route_score({"task_fit": 1.2}, {"task_fit": 1.0})
    with pytest.raises(ValueError):
        score_routes({"route-a": {"task_fit": 0.9}}, {})
    with pytest.raises(ValueError):
        scorecard_route({"route-a": {"task_fit": 0.9}}, {"task_fit": 1.0}, min_score=1.1)

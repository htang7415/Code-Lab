from __future__ import annotations

import pytest

from reasoning_evaluation import (
    majority_vote_gain,
    reasoning_accuracy,
    success_under_token_budget,
    successes_per_1k_tokens,
)


def test_reasoning_accuracy_and_efficiency_capture_quality_and_cost() -> None:
    correct = [1, 0, 1, 1]
    token_costs = [1800, 2000, 1600, 2200]
    assert reasoning_accuracy(correct) == pytest.approx(0.75)
    assert successes_per_1k_tokens(correct, token_costs) == pytest.approx(1000 * 3 / 7600)


def test_vote_gain_and_budgeted_success_are_simple_deltas_and_filters() -> None:
    assert majority_vote_gain(0.42, 0.55) == pytest.approx(0.13)
    assert success_under_token_budget([1, 0, 1, 1], [1800, 2000, 1600, 2200], 1900) == pytest.approx(
        1.0
    )


def test_reasoning_evaluation_validation_rejects_invalid_inputs() -> None:
    with pytest.raises(ValueError):
        reasoning_accuracy([1, 2])
    with pytest.raises(ValueError):
        successes_per_1k_tokens([1, 0], [1000])
    with pytest.raises(ValueError):
        majority_vote_gain(-0.1, 0.5)
    with pytest.raises(ValueError):
        success_under_token_budget([1], [0], 1000)

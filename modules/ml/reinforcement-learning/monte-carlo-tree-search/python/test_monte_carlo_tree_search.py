import math

import pytest

from monte_carlo_tree_search import uct_score


def test_uct_score_matches_mean_plus_exploration_bonus() -> None:
    score = uct_score(value_sum=1.2, parent_visits=10, child_visits=2, exploration=1.0)

    assert score == pytest.approx(1.6729830131446737)


def test_uct_score_prefers_unvisited_children() -> None:
    assert uct_score(value_sum=0.0, parent_visits=10, child_visits=0) == math.inf


def test_uct_score_requires_positive_parent_visits() -> None:
    with pytest.raises(ValueError, match="parent_visits"):
        uct_score(0.0, parent_visits=0, child_visits=1)

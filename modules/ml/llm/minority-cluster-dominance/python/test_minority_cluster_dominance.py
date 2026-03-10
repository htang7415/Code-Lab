from __future__ import annotations

import pytest

from minority_cluster_dominance import minority_cluster_dominance


def test_minority_cluster_dominance_returns_gap_between_top_two_minority_shares() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Berlin"]

    assert minority_cluster_dominance(answers) == pytest.approx(0.25)


def test_minority_cluster_dominance_returns_zero_when_minority_top_two_tie() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "rome", "Berlin"]

    assert minority_cluster_dominance(answers) == 0.0


def test_minority_cluster_dominance_returns_zero_when_no_minority_cluster_exists() -> None:
    assert minority_cluster_dominance(["Paris", "paris"]) == 0.0

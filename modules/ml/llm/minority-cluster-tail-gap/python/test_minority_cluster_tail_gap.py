from __future__ import annotations

import pytest

from minority_cluster_tail_gap import minority_cluster_tail_gap


def test_minority_cluster_tail_gap_returns_gap_between_top_two_tail_shares() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Rome", "Berlin"]

    assert minority_cluster_tail_gap(answers) == pytest.approx(1 / 3)


def test_minority_cluster_tail_gap_returns_one_for_single_tail_cluster() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome"]

    assert minority_cluster_tail_gap(answers) == 1.0


def test_minority_cluster_tail_gap_returns_zero_when_no_tail_exists() -> None:
    assert minority_cluster_tail_gap(["Paris", "paris", "London", "London"]) == 0.0

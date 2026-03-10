from __future__ import annotations

import pytest

from minority_cluster_tail_balance import minority_cluster_tail_balance


def test_minority_cluster_tail_balance_returns_ratio_for_tail_clusters() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Berlin", "Madrid", "Madrid"]

    assert minority_cluster_tail_balance(answers) == pytest.approx(0.5)


def test_minority_cluster_tail_balance_returns_one_for_single_tail_cluster() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome"]

    assert minority_cluster_tail_balance(answers) == 1.0


def test_minority_cluster_tail_balance_returns_zero_when_no_tail_exists() -> None:
    assert minority_cluster_tail_balance(["Paris", "paris", "London", "London"]) == 0.0

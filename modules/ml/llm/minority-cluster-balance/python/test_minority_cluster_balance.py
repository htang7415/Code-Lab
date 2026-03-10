from __future__ import annotations

import pytest

from minority_cluster_balance import minority_cluster_balance


def test_minority_cluster_balance_returns_ratio_between_smallest_and_largest_minority_clusters() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Berlin"]

    assert minority_cluster_balance(answers) == pytest.approx(0.5)


def test_minority_cluster_balance_returns_one_for_single_minority_cluster() -> None:
    answers = ["Paris", "paris", "paris", "London", "London"]

    assert minority_cluster_balance(answers) == 1.0


def test_minority_cluster_balance_returns_zero_when_no_minority_cluster_exists() -> None:
    assert minority_cluster_balance(["Paris", "paris"]) == 0.0

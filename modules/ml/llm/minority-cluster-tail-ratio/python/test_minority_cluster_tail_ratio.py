from __future__ import annotations

import pytest

from minority_cluster_tail_ratio import minority_cluster_tail_ratio


def test_minority_cluster_tail_ratio_returns_residual_tail_relative_to_strongest_minority() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Berlin"]

    assert minority_cluster_tail_ratio(answers) == pytest.approx(1.0)


def test_minority_cluster_tail_ratio_returns_zero_when_only_one_minority_cluster_exists() -> None:
    answers = ["Paris", "paris", "paris", "London", "London"]

    assert minority_cluster_tail_ratio(answers) == 0.0


def test_minority_cluster_tail_ratio_returns_zero_for_empty_answers() -> None:
    assert minority_cluster_tail_ratio([]) == 0.0

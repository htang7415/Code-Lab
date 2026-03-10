from __future__ import annotations

import math

import pytest

from minority_cluster_tail_entropy_gap import minority_cluster_tail_entropy_gap


def test_minority_cluster_tail_entropy_gap_returns_gap_from_uniform_tail_entropy() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Rome", "Berlin"]
    expected = math.log(2) + (2 / 3) * math.log(2 / 3) + (1 / 3) * math.log(1 / 3)

    assert minority_cluster_tail_entropy_gap(answers) == pytest.approx(expected)


def test_minority_cluster_tail_entropy_gap_returns_zero_for_single_tail_cluster() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome"]

    assert minority_cluster_tail_entropy_gap(answers) == 0.0


def test_minority_cluster_tail_entropy_gap_returns_zero_when_no_tail_exists() -> None:
    assert minority_cluster_tail_entropy_gap(["Paris", "paris", "London", "London"]) == 0.0

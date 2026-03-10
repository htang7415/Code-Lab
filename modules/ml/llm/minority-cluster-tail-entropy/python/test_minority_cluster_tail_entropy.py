from __future__ import annotations

import math

import pytest

from minority_cluster_tail_entropy import minority_cluster_tail_entropy


def test_minority_cluster_tail_entropy_returns_entropy_over_lower_mass_tail_clusters() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Berlin", "Madrid"]

    assert minority_cluster_tail_entropy(answers) == pytest.approx(math.log(3))


def test_minority_cluster_tail_entropy_returns_zero_when_tail_has_single_cluster() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome"]

    assert minority_cluster_tail_entropy(answers) == 0.0


def test_minority_cluster_tail_entropy_returns_zero_when_answers_are_empty() -> None:
    assert minority_cluster_tail_entropy([]) == 0.0

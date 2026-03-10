from __future__ import annotations

import math

import pytest

from minority_cluster_entropy import minority_cluster_entropy


def test_minority_cluster_entropy_returns_entropy_of_minority_mass() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Berlin"]

    expected = -(2 / 4) * math.log(2 / 4) - (1 / 4) * math.log(1 / 4) - (1 / 4) * math.log(1 / 4)
    assert minority_cluster_entropy(answers) == pytest.approx(expected)


def test_minority_cluster_entropy_handles_uneven_minority_clusters() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "rome", "Berlin"]

    expected = -(2 / 5) * math.log(2 / 5) - (2 / 5) * math.log(2 / 5) - (1 / 5) * math.log(1 / 5)
    assert minority_cluster_entropy(answers) == pytest.approx(expected)


def test_minority_cluster_entropy_returns_zero_when_no_minority_cluster_exists() -> None:
    assert minority_cluster_entropy(["Paris", "paris"]) == 0.0

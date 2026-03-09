from __future__ import annotations

from minority_cluster_mode import minority_cluster_mode


def test_minority_cluster_mode_returns_most_common_minority_cluster_size() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Berlin"]

    assert minority_cluster_mode(answers) == 1


def test_minority_cluster_mode_handles_repeated_minority_cluster_sizes() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "rome", "Berlin"]

    assert minority_cluster_mode(answers) == 2


def test_minority_cluster_mode_returns_zero_when_no_minority_cluster_exists() -> None:
    assert minority_cluster_mode(["Paris", "paris"]) == 0

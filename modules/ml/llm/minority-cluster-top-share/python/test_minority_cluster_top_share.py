from __future__ import annotations

import pytest

from minority_cluster_top_share import minority_cluster_top_share


def test_minority_cluster_top_share_returns_largest_minority_share() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Berlin"]

    assert minority_cluster_top_share(answers) == pytest.approx(0.5)


def test_minority_cluster_top_share_handles_uneven_minority_sizes() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "rome", "Berlin"]

    assert minority_cluster_top_share(answers) == pytest.approx(0.4)


def test_minority_cluster_top_share_returns_zero_when_no_minority_cluster_exists() -> None:
    assert minority_cluster_top_share(["Paris", "paris"]) == 0.0

from __future__ import annotations

import pytest

from minority_cluster_tail_share import minority_cluster_tail_share


def test_minority_cluster_tail_share_returns_absolute_share_of_strongest_tail_cluster() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Rome", "Berlin"]

    assert minority_cluster_tail_share(answers) == pytest.approx(0.25)


def test_minority_cluster_tail_share_returns_small_share_for_single_tail_cluster() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome"]

    assert minority_cluster_tail_share(answers) == pytest.approx(1 / 6)


def test_minority_cluster_tail_share_returns_zero_when_no_tail_exists() -> None:
    assert minority_cluster_tail_share(["Paris", "paris", "London", "London"]) == 0.0

from __future__ import annotations

from minority_cluster_count import minority_cluster_count


def test_minority_cluster_count_counts_clusters_outside_the_largest_one() -> None:
    assert minority_cluster_count(["Paris", "the paris", "London", "Rome"]) == 2


def test_minority_cluster_count_returns_zero_for_single_cluster() -> None:
    assert minority_cluster_count(["Paris", "paris"]) == 0


def test_minority_cluster_count_returns_zero_for_empty_input() -> None:
    assert minority_cluster_count([]) == 0

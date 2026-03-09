from __future__ import annotations

import pytest

from minority_cluster_share import minority_cluster_share


def test_minority_cluster_share_normalizes_minority_cluster_count() -> None:
    share = minority_cluster_share(["Paris", "the paris", "London", "Rome"])

    assert share == pytest.approx(2 / 3)


def test_minority_cluster_share_returns_zero_for_single_cluster() -> None:
    assert minority_cluster_share(["Paris", "paris"]) == 0.0


def test_minority_cluster_share_returns_zero_for_empty_input() -> None:
    assert minority_cluster_share([]) == 0.0

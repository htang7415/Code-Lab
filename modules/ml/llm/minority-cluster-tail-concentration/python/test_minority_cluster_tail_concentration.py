from __future__ import annotations

import pytest

from minority_cluster_tail_concentration import minority_cluster_tail_concentration


def test_minority_cluster_tail_concentration_returns_herfindahl_style_tail_concentration() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Rome", "Berlin"]

    assert minority_cluster_tail_concentration(answers) == pytest.approx(5 / 9)


def test_minority_cluster_tail_concentration_returns_one_for_single_tail_cluster() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome"]

    assert minority_cluster_tail_concentration(answers) == 1.0


def test_minority_cluster_tail_concentration_returns_zero_when_no_tail_exists() -> None:
    assert minority_cluster_tail_concentration(["Paris", "paris", "London", "London"]) == 0.0

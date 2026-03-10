from __future__ import annotations

import pytest

from minority_cluster_residual_mass import minority_cluster_residual_mass


def test_minority_cluster_residual_mass_returns_mass_left_after_strongest_minority_cluster() -> None:
    answers = ["Paris", "paris", "paris", "London", "London", "Rome", "Berlin"]

    assert minority_cluster_residual_mass(answers) == pytest.approx(2 / 7)


def test_minority_cluster_residual_mass_returns_zero_when_only_one_minority_cluster_exists() -> None:
    answers = ["Paris", "paris", "paris", "London", "London"]

    assert minority_cluster_residual_mass(answers) == 0.0


def test_minority_cluster_residual_mass_returns_zero_for_empty_answers() -> None:
    assert minority_cluster_residual_mass([]) == 0.0

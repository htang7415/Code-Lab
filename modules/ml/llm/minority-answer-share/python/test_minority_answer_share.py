from __future__ import annotations

import pytest

from minority_answer_share import minority_answer_share


def test_minority_answer_share_returns_mass_outside_largest_cluster() -> None:
    share = minority_answer_share(["Paris", "the paris", "London", "Rome"])

    assert share == pytest.approx(0.5)


def test_minority_answer_share_returns_zero_for_unanimous_answers() -> None:
    assert minority_answer_share(["Paris", "paris"]) == 0.0


def test_minority_answer_share_returns_zero_for_empty_input() -> None:
    assert minority_answer_share([]) == 0.0

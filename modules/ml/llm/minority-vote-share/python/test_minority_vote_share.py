from __future__ import annotations

import pytest

from minority_vote_share import minority_vote_share


def test_minority_vote_share_returns_complement_of_largest_cluster() -> None:
    share = minority_vote_share(["Paris", "the paris", "London", "Rome"])

    assert share == pytest.approx(0.5)


def test_minority_vote_share_returns_zero_for_unanimous_answers() -> None:
    assert minority_vote_share(["Paris", "paris"]) == 0.0


def test_minority_vote_share_returns_zero_for_empty_input() -> None:
    assert minority_vote_share([]) == 0.0

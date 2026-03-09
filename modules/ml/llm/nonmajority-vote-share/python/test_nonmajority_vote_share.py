import pytest

from nonmajority_vote_share import nonmajority_vote_share


def test_nonmajority_vote_share_returns_complement_of_top_vote_share() -> None:
    score = nonmajority_vote_share(["Paris", "the paris", "London", "Rome"])

    assert score == pytest.approx(0.5)


def test_nonmajority_vote_share_is_zero_when_all_answers_match() -> None:
    assert nonmajority_vote_share(["Answer", "answer", "the answer"]) == pytest.approx(0.0)


def test_nonmajority_vote_share_returns_zero_for_empty_answers() -> None:
    assert nonmajority_vote_share([]) == pytest.approx(0.0)

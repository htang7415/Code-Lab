import pytest

from vote_tail_mass import vote_tail_mass


def test_vote_tail_mass_returns_complement_of_top_vote_share() -> None:
    score = vote_tail_mass(["Paris", "the paris", "London", "Rome"])

    assert score == pytest.approx(0.5)


def test_vote_tail_mass_is_zero_when_all_answers_match() -> None:
    assert vote_tail_mass(["Answer", "answer", "the answer"]) == pytest.approx(0.0)


def test_vote_tail_mass_returns_zero_for_empty_answers() -> None:
    assert vote_tail_mass([]) == pytest.approx(0.0)

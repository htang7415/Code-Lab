import pytest

from vote_imbalance import vote_imbalance


def test_vote_imbalance_returns_normalized_gap_between_top_two_counts() -> None:
    score = vote_imbalance(["Paris", "the paris", "London", "Rome"])

    assert score == pytest.approx(1.0 / 3.0)


def test_vote_imbalance_is_one_when_all_answers_match() -> None:
    assert vote_imbalance(["Answer", "answer", "the answer"]) == pytest.approx(1.0)


def test_vote_imbalance_returns_zero_for_empty_answers() -> None:
    assert vote_imbalance([]) == pytest.approx(0.0)

from vote_frequency_gap import vote_frequency_gap


def test_vote_frequency_gap_returns_top_count_minus_runner_up_count() -> None:
    assert vote_frequency_gap(["Paris", "the paris", "London", "Rome"]) == 1


def test_vote_frequency_gap_returns_full_count_when_all_answers_match() -> None:
    assert vote_frequency_gap(["Answer", "answer", "the answer"]) == 3


def test_vote_frequency_gap_returns_zero_for_empty_answers() -> None:
    assert vote_frequency_gap([]) == 0

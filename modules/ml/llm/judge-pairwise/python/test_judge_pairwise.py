import pytest

from judge_pairwise import pairwise_judge_rates


def test_pairwise_judge_rates_returns_win_loss_tie_fractions() -> None:
    win_rate, loss_rate, tie_rate = pairwise_judge_rates([1, 1, 0, -1])

    assert win_rate == 0.5
    assert loss_rate == 0.25
    assert tie_rate == 0.25


def test_pairwise_judge_rates_handles_empty_input() -> None:
    assert pairwise_judge_rates([]) == (0.0, 0.0, 0.0)


def test_pairwise_judge_rates_validates_outcome_values() -> None:
    with pytest.raises(ValueError, match="only -1, 0, or 1"):
        pairwise_judge_rates([2])

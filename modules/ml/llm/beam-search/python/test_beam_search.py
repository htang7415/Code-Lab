import pytest

from beam_search import beam_search_step


def test_beam_search_step_keeps_top_scoring_expansions() -> None:
    beams = [([0], 0.0)]
    next_token_log_probs = [[-0.1, -0.5, -1.0]]

    updated = beam_search_step(beams, next_token_log_probs, beam_width=2)

    assert updated == [([0, 0], -0.1), ([0, 1], -0.5)]


def test_beam_search_step_ranks_candidates_across_all_beams() -> None:
    beams = [([1], -0.2), ([2], -0.1)]
    next_token_log_probs = [[-0.1, -1.0], [-0.4, -0.2]]

    updated = beam_search_step(beams, next_token_log_probs, beam_width=3)

    assert updated == [([1, 0], -0.30000000000000004), ([2, 1], -0.30000000000000004), ([2, 0], -0.5)]


def test_beam_search_step_requires_matching_inputs() -> None:
    with pytest.raises(ValueError, match="same length"):
        beam_search_step([([0], 0.0)], [], beam_width=1)

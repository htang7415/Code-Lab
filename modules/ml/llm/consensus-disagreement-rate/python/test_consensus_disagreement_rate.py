import pytest

from consensus_disagreement_rate import consensus_disagreement_rate


def test_consensus_disagreement_rate_uses_normalized_answers() -> None:
    rate = consensus_disagreement_rate(["The Eiffel Tower!", "eiffel tower", "Paris"])

    assert rate == pytest.approx(1.0 / 3.0)


def test_consensus_disagreement_rate_is_zero_for_unanimous_answers() -> None:
    assert consensus_disagreement_rate(["yes", "yes"]) == pytest.approx(0.0)


def test_consensus_disagreement_rate_is_high_when_all_answers_differ() -> None:
    assert consensus_disagreement_rate(["a", "b", "c"]) == pytest.approx(2.0 / 3.0)

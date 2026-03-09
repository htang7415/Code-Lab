import pytest

from exact_match import exact_match_score


def test_exact_match_score_normalizes_case_articles_and_punctuation() -> None:
    score = exact_match_score(
        predictions=[" The Eiffel Tower! ", "Seattle"],
        labels=["eiffel tower", " seattle "],
    )

    assert score == 1.0


def test_exact_match_score_detects_real_mismatch() -> None:
    score = exact_match_score(
        predictions=["Madison", "Chicago"],
        labels=["Madison", "Milwaukee"],
    )

    assert score == 0.5


def test_exact_match_score_requires_same_length_inputs() -> None:
    with pytest.raises(ValueError, match="same length"):
        exact_match_score(["a"], ["a", "b"])

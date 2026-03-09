import pytest

from macro_f1 import macro_f1_score


def test_macro_f1_score_averages_per_class_f1_values() -> None:
    score = macro_f1_score(
        true_positives=[8, 1],
        false_positives=[2, 1],
        false_negatives=[0, 3],
    )

    assert score == pytest.approx(0.6111111111)


def test_macro_f1_score_returns_zero_for_no_classes() -> None:
    assert macro_f1_score([], [], []) == pytest.approx(0.0)


def test_macro_f1_score_requires_matching_lengths() -> None:
    with pytest.raises(ValueError, match="same length"):
        macro_f1_score([1], [0, 1], [0])

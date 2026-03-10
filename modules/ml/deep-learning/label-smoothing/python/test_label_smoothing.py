import math

import pytest

from label_smoothing import label_smoothed_cross_entropy


def test_label_smoothed_cross_entropy_matches_cross_entropy_when_smoothing_is_zero() -> None:
    loss = label_smoothed_cross_entropy([0.8, 0.2], target_index=0, smoothing=0.0)

    assert loss == pytest.approx(-math.log(0.8))


def test_label_smoothed_cross_entropy_penalizes_overconfidence_less_sharply() -> None:
    smoothed = label_smoothed_cross_entropy([0.8, 0.2], target_index=0, smoothing=0.1)
    unsmoothed = label_smoothed_cross_entropy([0.8, 0.2], target_index=0, smoothing=0.0)

    assert smoothed > unsmoothed


def test_label_smoothed_cross_entropy_requires_normalized_probabilities() -> None:
    with pytest.raises(ValueError, match="sum to 1"):
        label_smoothed_cross_entropy([0.8, 0.3], target_index=0, smoothing=0.1)

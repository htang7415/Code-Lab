import pytest

from importance_sampling import importance_sampling_estimate


def test_importance_sampling_estimate_matches_weighted_average() -> None:
    estimate = importance_sampling_estimate(
        rewards=[1.0, 0.0, 2.0],
        target_probs=[0.5, 0.25, 0.5],
        behavior_probs=[0.25, 0.5, 0.25],
    )

    assert estimate == pytest.approx(2.0)


def test_importance_sampling_estimate_returns_zero_for_no_samples() -> None:
    assert importance_sampling_estimate([], [], []) == 0.0


def test_importance_sampling_estimate_requires_positive_behavior_probs() -> None:
    with pytest.raises(ValueError, match="strictly positive"):
        importance_sampling_estimate([1.0], [0.5], [0.0])

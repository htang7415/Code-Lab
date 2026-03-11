import pytest

from two_sample_t_test import t_stat


def test_t_stat_sign_matches_mean_difference() -> None:
    assert t_stat([1, 1, 1], [2, 2, 2]) < 0


def test_t_stat_handles_zero_variance_with_equal_means() -> None:
    assert t_stat([1, 1, 1], [1, 1, 1]) == 0.0


def test_t_stat_requires_at_least_two_observations_per_group() -> None:
    with pytest.raises(ValueError, match="at least 2 observations"):
        t_stat([1.0], [2.0, 3.0])

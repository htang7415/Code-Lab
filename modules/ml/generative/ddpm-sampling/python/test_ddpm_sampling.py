import pytest

from ddpm_sampling import ddpm_reverse_mean


def test_ddpm_reverse_mean_matches_reverse_step_formula() -> None:
    value = ddpm_reverse_mean(
        x_t=0.8,
        predicted_noise=0.3,
        alpha_t=0.9,
        alpha_bar_t=0.81,
        beta_t=0.1,
    )

    assert value == pytest.approx(0.7707264177005667)


def test_ddpm_reverse_mean_allows_zero_beta() -> None:
    value = ddpm_reverse_mean(
        x_t=1.2,
        predicted_noise=0.5,
        alpha_t=0.81,
        alpha_bar_t=0.64,
        beta_t=0.0,
    )

    assert value == pytest.approx(1.3333333333333333)


def test_ddpm_reverse_mean_validates_schedule_relationship() -> None:
    with pytest.raises(ValueError, match="must not exceed"):
        ddpm_reverse_mean(0.5, 0.1, alpha_t=0.8, alpha_bar_t=0.9, beta_t=0.2)

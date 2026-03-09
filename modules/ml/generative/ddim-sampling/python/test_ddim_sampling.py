import pytest

from ddim_sampling import ddim_step


def test_ddim_step_matches_deterministic_update() -> None:
    value = ddim_step(
        x_t=0.8,
        predicted_noise=0.3,
        alpha_bar_t=0.64,
        alpha_bar_prev=0.81,
    )

    assert value == pytest.approx(0.8282669683062203)


def test_ddim_step_returns_same_point_when_schedule_does_not_change() -> None:
    value = ddim_step(
        x_t=0.75,
        predicted_noise=0.2,
        alpha_bar_t=0.81,
        alpha_bar_prev=0.81,
    )

    assert value == pytest.approx(0.75)


def test_ddim_step_requires_reverse_schedule_order() -> None:
    with pytest.raises(ValueError, match="at least"):
        ddim_step(0.5, 0.1, alpha_bar_t=0.81, alpha_bar_prev=0.64)

from __future__ import annotations

import math


def ddpm_reverse_mean(
    x_t: float,
    predicted_noise: float,
    alpha_t: float,
    alpha_bar_t: float,
    beta_t: float,
) -> float:
    if not 0.0 < alpha_t <= 1.0:
        raise ValueError("alpha_t must satisfy 0 < alpha_t <= 1")
    if not 0.0 < alpha_bar_t < 1.0:
        raise ValueError("alpha_bar_t must satisfy 0 < alpha_bar_t < 1")
    if alpha_bar_t > alpha_t:
        raise ValueError("alpha_bar_t must not exceed alpha_t")
    if not 0.0 <= beta_t < 1.0:
        raise ValueError("beta_t must satisfy 0 <= beta_t < 1")

    return (
        x_t - (beta_t / math.sqrt(1.0 - alpha_bar_t)) * predicted_noise
    ) / math.sqrt(alpha_t)

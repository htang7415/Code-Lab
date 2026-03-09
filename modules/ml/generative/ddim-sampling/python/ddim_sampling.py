from __future__ import annotations

import math


def ddim_step(
    x_t: float,
    predicted_noise: float,
    alpha_bar_t: float,
    alpha_bar_prev: float,
) -> float:
    if not 0.0 < alpha_bar_t < 1.0:
        raise ValueError("alpha_bar_t must satisfy 0 < alpha_bar_t < 1")
    if not 0.0 < alpha_bar_prev <= 1.0:
        raise ValueError("alpha_bar_prev must satisfy 0 < alpha_bar_prev <= 1")
    if alpha_bar_prev < alpha_bar_t:
        raise ValueError("alpha_bar_prev must be at least alpha_bar_t")

    x0_hat = (x_t - math.sqrt(1.0 - alpha_bar_t) * predicted_noise) / math.sqrt(alpha_bar_t)
    return math.sqrt(alpha_bar_prev) * x0_hat + math.sqrt(1.0 - alpha_bar_prev) * predicted_noise

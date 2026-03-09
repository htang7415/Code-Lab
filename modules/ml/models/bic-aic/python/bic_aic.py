from __future__ import annotations

import math


def aic_bic(
    log_likelihood: float,
    num_params: int,
    num_samples: int,
) -> tuple[float, float]:
    if num_params < 0:
        raise ValueError("num_params must be non-negative")
    if num_samples <= 0:
        raise ValueError("num_samples must be positive")

    aic = 2.0 * num_params - 2.0 * log_likelihood
    bic = num_params * math.log(num_samples) - 2.0 * log_likelihood
    return aic, bic

from __future__ import annotations

import math


def _harmonic_number(n: int) -> float:
    return sum(1.0 / k for k in range(1, n + 1))


def average_path_length(sample_size: int) -> float:
    if sample_size <= 1:
        return 0.0
    return 2.0 * _harmonic_number(sample_size - 1) - (2.0 * (sample_size - 1) / sample_size)


def isolation_score(avg_path_length: float, sample_size: int) -> float:
    if avg_path_length < 0.0:
        raise ValueError("avg_path_length must be non-negative")
    if sample_size <= 1:
        raise ValueError("sample_size must be greater than 1")

    normalizer = average_path_length(sample_size)
    return 2.0 ** (-avg_path_length / normalizer)

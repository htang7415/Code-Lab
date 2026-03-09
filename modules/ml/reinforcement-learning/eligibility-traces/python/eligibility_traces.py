from __future__ import annotations


def eligibility_trace_step(
    previous_trace: float,
    feature_value: float,
    gamma: float,
    lam: float,
) -> float:
    if not 0.0 <= gamma <= 1.0:
        raise ValueError("gamma must satisfy 0 <= gamma <= 1")
    if not 0.0 <= lam <= 1.0:
        raise ValueError("lam must satisfy 0 <= lam <= 1")

    return gamma * lam * previous_trace + feature_value

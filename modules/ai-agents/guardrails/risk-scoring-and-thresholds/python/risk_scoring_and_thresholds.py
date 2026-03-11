from __future__ import annotations


def weighted_risk_score(signals: dict[str, float], weights: dict[str, float]) -> float:
    if not signals:
        raise ValueError("signals must be non-empty")
    if not weights:
        raise ValueError("weights must be non-empty")

    weighted_sum = 0.0
    total_weight = 0.0
    for signal_name, signal_value in signals.items():
        cleaned_signal = signal_name.strip()
        if not cleaned_signal:
            raise ValueError("signal names must be non-empty")
        if cleaned_signal not in weights:
            raise ValueError(f"missing weight for signal: {cleaned_signal}")
        if not 0.0 <= signal_value <= 1.0:
            raise ValueError("signal values must satisfy 0 <= value <= 1")

        weight = weights[cleaned_signal]
        if weight <= 0.0:
            raise ValueError("weights must be positive")
        weighted_sum += signal_value * weight
        total_weight += weight

    return weighted_sum / total_weight


def active_risk_signals(signals: dict[str, float], min_signal: float) -> list[str]:
    if not 0.0 <= min_signal <= 1.0:
        raise ValueError("min_signal must satisfy 0 <= value <= 1")

    active: list[str] = []
    for signal_name, signal_value in signals.items():
        cleaned_signal = signal_name.strip()
        if not cleaned_signal:
            raise ValueError("signal names must be non-empty")
        if not 0.0 <= signal_value <= 1.0:
            raise ValueError("signal values must satisfy 0 <= value <= 1")
        if signal_value >= min_signal:
            active.append(cleaned_signal)
    return sorted(active)


def risk_decision(score: float, review_threshold: float, block_threshold: float) -> str:
    if not 0.0 <= score <= 1.0:
        raise ValueError("score must satisfy 0 <= value <= 1")
    if not 0.0 <= review_threshold <= 1.0:
        raise ValueError("review_threshold must satisfy 0 <= value <= 1")
    if not 0.0 <= block_threshold <= 1.0:
        raise ValueError("block_threshold must satisfy 0 <= value <= 1")
    if review_threshold > block_threshold:
        raise ValueError("review_threshold must be smaller than or equal to block_threshold")

    if score >= block_threshold:
        return "block"
    if score >= review_threshold:
        return "review"
    return "allow"

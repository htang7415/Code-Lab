from __future__ import annotations


def split_traffic(total: int, canary_pct: float) -> tuple[int, int]:
    if total < 0:
        raise ValueError("total must be non-negative")
    if not 0.0 <= canary_pct <= 1.0:
        raise ValueError("canary_pct must satisfy 0 <= canary_pct <= 1")

    canary = int(total * canary_pct)
    return canary, total - canary


def next_canary_share(current_share: float, step: float, error_rate: float, threshold: float) -> float:
    if not 0.0 <= current_share <= 1.0:
        raise ValueError("current_share must satisfy 0 <= current_share <= 1")
    if not 0.0 < step <= 1.0:
        raise ValueError("step must satisfy 0 < step <= 1")
    if not 0.0 <= error_rate <= 1.0:
        raise ValueError("error_rate must satisfy 0 <= error_rate <= 1")
    if not 0.0 <= threshold <= 1.0:
        raise ValueError("threshold must satisfy 0 <= threshold <= 1")

    if error_rate <= threshold:
        return min(1.0, current_share + step)
    return max(0.0, current_share - step)


def shadow_disagreement_rate(live_predictions: list[object], shadow_predictions: list[object]) -> tuple[int, float]:
    if len(live_predictions) != len(shadow_predictions):
        raise ValueError("live_predictions and shadow_predictions must have the same length")
    if not live_predictions:
        return 0, 0.0

    disagreements = sum(live != shadow for live, shadow in zip(live_predictions, shadow_predictions))
    return disagreements, disagreements / len(live_predictions)


def backfill_replay_metrics(
    logged_requests: int,
    replayed_requests: int,
    mismatched_outputs: int,
) -> tuple[float, float]:
    if logged_requests <= 0:
        raise ValueError("logged_requests must be positive")
    if not 0 <= replayed_requests <= logged_requests:
        raise ValueError("replayed_requests must satisfy 0 <= replayed_requests <= logged_requests")
    if not 0 <= mismatched_outputs <= replayed_requests:
        raise ValueError("mismatched_outputs must satisfy 0 <= mismatched_outputs <= replayed_requests")

    coverage = replayed_requests / logged_requests
    mismatch_rate = 0.0 if replayed_requests == 0 else mismatched_outputs / replayed_requests
    return coverage, mismatch_rate


def is_online(latency_ms: float, threshold_ms: float = 100.0) -> bool:
    if latency_ms < 0.0:
        raise ValueError("latency_ms must be non-negative")
    if threshold_ms <= 0.0:
        raise ValueError("threshold_ms must be positive")
    return latency_ms <= threshold_ms


def choose_mode(batch_size: int) -> str:
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    return "batch" if batch_size > 1 else "realtime"

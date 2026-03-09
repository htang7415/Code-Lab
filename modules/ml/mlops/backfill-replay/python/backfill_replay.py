from __future__ import annotations


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

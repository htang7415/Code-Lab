from __future__ import annotations

import pytest

from rollout_and_serving_modes import (
    backfill_replay_metrics,
    choose_mode,
    is_online,
    next_canary_share,
    shadow_disagreement_rate,
    split_traffic,
)


def test_split_traffic_returns_canary_and_baseline_counts() -> None:
    assert split_traffic(total=100, canary_pct=0.2) == (20, 80)


def test_split_traffic_validates_range() -> None:
    with pytest.raises(ValueError, match="canary_pct"):
        split_traffic(total=10, canary_pct=1.2)


def test_next_canary_share_advances_when_healthy() -> None:
    assert next_canary_share(0.2, 0.1, error_rate=0.01, threshold=0.02) == pytest.approx(0.3)


def test_next_canary_share_rolls_back_when_breached() -> None:
    assert next_canary_share(0.2, 0.1, error_rate=0.03, threshold=0.02) == pytest.approx(0.1)


def test_shadow_disagreement_rate_counts_mismatches() -> None:
    disagreements, fraction = shadow_disagreement_rate([1, 0, 1], [1, 1, 0])
    assert disagreements == 2
    assert fraction == pytest.approx(2 / 3)


def test_backfill_replay_metrics_returns_coverage_and_mismatch() -> None:
    coverage, mismatch = backfill_replay_metrics(100, 80, 8)
    assert coverage == 0.8
    assert mismatch == 0.1


def test_is_online_uses_threshold() -> None:
    assert is_online(50.0, threshold_ms=100.0) is True
    assert is_online(120.0, threshold_ms=100.0) is False


def test_choose_mode_uses_batch_size() -> None:
    assert choose_mode(1) == "realtime"
    assert choose_mode(8) == "batch"

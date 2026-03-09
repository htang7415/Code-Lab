import pytest

from backfill_replay import backfill_replay_metrics


def test_backfill_replay_metrics_report_coverage_and_mismatch_rate() -> None:
    coverage, mismatch_rate = backfill_replay_metrics(
        logged_requests=100,
        replayed_requests=80,
        mismatched_outputs=4,
    )

    assert coverage == pytest.approx(0.8)
    assert mismatch_rate == pytest.approx(0.05)


def test_backfill_replay_metrics_allow_zero_replayed_requests() -> None:
    coverage, mismatch_rate = backfill_replay_metrics(
        logged_requests=100,
        replayed_requests=0,
        mismatched_outputs=0,
    )

    assert coverage == pytest.approx(0.0)
    assert mismatch_rate == pytest.approx(0.0)


def test_backfill_replay_metrics_require_valid_counts() -> None:
    with pytest.raises(ValueError, match="mismatched_outputs"):
        backfill_replay_metrics(logged_requests=10, replayed_requests=5, mismatched_outputs=6)

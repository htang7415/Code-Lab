from __future__ import annotations

import pytest

from breach_bucket_wave import breach_bucket_wave


def test_breach_bucket_wave_counts_direction_changes_in_bucket_shares() -> None:
    wave = breach_bucket_wave([1.02, 1.15, 1.16, 1.17, 1.4], capacity=1.0, cutoffs=[0.05, 0.2])

    assert wave == 1


def test_breach_bucket_wave_returns_zero_for_monotonic_bucket_profile() -> None:
    assert breach_bucket_wave([1.05, 1.06, 1.08, 1.2], capacity=1.0, cutoffs=[0.1, 0.3]) == 0


def test_breach_bucket_wave_rejects_unsorted_cutoffs() -> None:
    with pytest.raises(ValueError, match="cutoffs"):
        breach_bucket_wave([1.2], capacity=1.0, cutoffs=[0.3, 0.1])

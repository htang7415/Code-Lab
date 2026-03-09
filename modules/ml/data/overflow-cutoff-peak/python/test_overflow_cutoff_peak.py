from __future__ import annotations

import pytest

from overflow_cutoff_peak import overflow_cutoff_peak


def test_overflow_cutoff_peak_returns_worst_qualifying_overflow() -> None:
    peak = overflow_cutoff_peak([64, 120, 111, 200], max_length=100, cutoff=20)

    assert peak == 100


def test_overflow_cutoff_peak_returns_zero_when_no_case_reaches_cutoff() -> None:
    assert overflow_cutoff_peak([64, 105, 111], max_length=100, cutoff=20) == 0


def test_overflow_cutoff_peak_rejects_negative_lengths() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        overflow_cutoff_peak([64, -1], max_length=100, cutoff=20)

from __future__ import annotations

import pytest

from overflow_cutoff_tail_mass import overflow_cutoff_tail_mass


def test_overflow_cutoff_tail_mass_returns_share_of_mass_in_upper_tail() -> None:
    lengths = [120, 120, 180, 180]

    assert overflow_cutoff_tail_mass(lengths, max_length=100, cutoff=20, quantile=0.5) == pytest.approx(0.8)


def test_overflow_cutoff_tail_mass_returns_zero_when_nothing_qualifies() -> None:
    assert overflow_cutoff_tail_mass([105, 110], max_length=100, cutoff=20) == 0.0


def test_overflow_cutoff_tail_mass_rejects_invalid_quantile() -> None:
    with pytest.raises(ValueError, match="quantile"):
        overflow_cutoff_tail_mass([120], max_length=100, cutoff=20, quantile=1.1)
